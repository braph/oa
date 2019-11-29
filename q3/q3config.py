#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

''' Quake 3 configuration file parser '''
# Since we want to preserve as much syntax of the original config file
# as possible, we tokenize the configuration string and create a doubly-linked
# list of all the tokens.
# When we edit the configuration file later, we only change the specific
# tokens we're intrested in.
# In the end, we put all tokens together and get a new configuration string.
# Since fiddling with the token list itself is cumbersome `View`-classes are
# provided.

try:    range = xrange # Python2
except: pass
try:    FileNotFoundError = FileNotFoundError
except: FileNotFoundError = IOError # Python2

from re import compile as RE, VERBOSE as __RE_VERBOSE
from itertools import islice

GRAMMAR = RE(r'''
(?# === Most-likely first === )

 (?# A Comment)
    (?: //[^\n]* )
|(?# A Word)
    (?: [^\s";]+ (?=//)) |
    (?: [^\s";]+)
|(?# Quoted Word - Ending Quote can be omitted)
    (?: " [^"\n]* "? )
|(?# Whitespace)
     [ \t\f\v]+
|(?# Newline)
     \n
|(?# Semicolon)
     ;
''', __RE_VERBOSE)

class Token:
    '''
    Base token class which provides functionality such as appending, dropping
    and iterating over tokens.
    '''

    __slots__ = 'prev', 'next'
    def __init__(self):
        self.prev = None
        self.next = None

    def drop(self, end=None):
        '''
        Drop this token from the list.

        token.drop(end):
            [...] [token] [...] [end] [...]
                  `-----------------'
        '''
        end  = end or self
        prev = self.prev
        next = end.next
        if prev is not None: prev.next = next
        if next is not None: next.prev = prev
        self.prev = end.next = None

    def prepend(self, start, end=None):
        '''
        Prepend a token.

        token.prepend(start, end):
            [token.prev]                             [token]
                         `-- [start] [...] [end] --'
        '''
        end = end or start
        if start.prev is not None: raise Exception('Start token already linked')
        if end.next is not None:   raise Exception('End token already linked')

        if self.prev is not None:
            start.prev = self.prev
            self.prev.next = start

        end.next = self
        self.prev = end
        #self.assert_valid_links()
        return None

    def append(self, start, end=None):
        '''
        Append a token. (Returns `end`)

        token.append(start, end):
            [token]                             [token.next]
                    `-- [start] [...] [end] --'
        '''
        end = end or start
        if start.prev is not None: raise Exception('Start token already linked')
        if end.next is not None:   raise Exception('End token already linked')

        if self.next is not None:
            end.next = self.next
            self.next.prev = end

        start.prev = self
        self.next = start
        #self.assert_valid_links()
        return end

    def strTo(self, end=None): # TODO?
        if end: return ''.join(map(str, self.findIter(end=end)))
        else:   return ''.join(map(str, self))

    def dump(self):
        t = self
        while t:
            print(type(t), str(t), end=' --> ')
            t = t.next
        print()

    def ensure_token(self, token_type=None, *args):
        '''
        Ensures that the token is of `token_type`.

        If so, return current token.
        Otherwise, append a new token of `token_type(*args)` or `token_type[0](*args)` and return it.
        '''
        if isinstance(self, token_type):
            return self
        try:    tok = token_type(*args)
        except: tok = token_type[0](*args)
        return  self.insert(tok)

    def __iter__(self):
        ''' Iterate over all tokens. '''
        next = self
        while next is not None:
            yield next
            next = next.next

    iter = __iter__

    def findNext(self, cond=None, end=None, include_self=False):
        '''
        Find next token matching `cond(token)` between current token and `end(token)`.
        '''
        next = self if include_self else self.next
        if end:
            if cond:
                while next is not None and not end(next):
                    if cond(next):
                        return next
                    next = next.next
            else:
                if next is not None and not end(next):
                    return next
        elif cond:
            while next is not None:
                if cond(next):
                    return next
                next = next.next
        else:
            return next

        return None

    def findIter(self, cond=None, end=None, skip_this=False):
        '''
        Iter over all tokens matching `cond(token)` until `end(token)`.

        Use `iter()` for the case `cond==None and end==None`.
        '''
        next = self.next if skip_this else self
        if end:
            if cond:
                while next is not None and not end(next):
                    if cond(next):
                        yield next
                    next = next.next
            else:
                while next is not None and not end(next):
                    yield next
                    next = next.next
        else:
            while next is not None:
                if cond(next):
                    yield next
                next = next.next

    def last(self):
        ''' Return the last token '''
        next = self
        while next.next is not None:
            next = next.next
        return next
        
    def assert_valid_links(self):
        t = self
        while t:
            if t.next: assert t.next.prev == t
            if t.prev: assert t.prev.next == t
            t = t.next
        t = self
        while t:
            if t.next: assert t.next.prev == t
            if t.prev: assert t.prev.next == t
            t = t.prev

class TWord(Token):
    __slots__ = 's'
    ''' A Word without quoting (they will only be added if needed). '''
    def __init__(self, s):
        self.prev = None
        self.next = None
        self.s = s

    @staticmethod
    def word_for_conf(s, forceQuotes=False):
        if (forceQuotes or 
                ((s == '')) or ((' ' in s)) or ((';' in s)) or (('//' in s))):
            return '"' + s + '"'
        else:
            return s

    def __str__(self):
        return TWord.word_for_conf(self.s)
    def __repr__(self):
        return repr(self.s)

class TQuoted(TWord):
    __slots__ = ()
    ''' A Word that enforces quoting. '''
    def __str__(self):
        return TWord.word_for_conf(self.s, True)

class TComment(Token):
    __slots__ = 's'
    def __init__(self, s):
        self.prev = None
        self.next = None
        self.s = s
    def __str__(self):
        return '//' + self.s
    def __repr__(self):
        return self.__str__()

class TWhitespace(Token):
    __slots__ = 's'
    def __init__(self, s):
        self.prev = None
        self.next = None
        self.s = s
    def __str__(self):
        return self.s

class TNewline(Token):
    __slots__ = ()
    def __str__(self):
        return '\n'

class TSemicolon(Token):
    __slots__ = ()
    def __str__(self):
        return ';'

class TEmpty(Token):
    __slots__ = ()
    ''' This is a helper class. '''
    def __init__(self, next=None):
        self.next = None
        self.prev = None
        if next is not None: self.append(next)
    def __str__(self):
        return ''

# === Conditionals for `findNext` and `findIter`
def isTWord(token):
    ''' Conditional `isinstance(token, TWord)`. '''
    return isinstance(token, TWord)

def isCommandEnd(token):
    ''' Conditional `isinstance(token, (TNewline, TSemicolon, TComment)`.
    Leading whitespace in front of a comment will be preserved. '''
    return isinstance(token, (TSemicolon, TNewline, TComment)) or (
           isinstance(token, TWhitespace) and isinstance(token.next, TComment))


class Q3BaseView(object):
    ''' Abstract class for implementing viewers on tokens '''
    end   = NotImplemented
    begin = NotImplemented
    drop  = NotImplemented

    def __init__(self, token):
        self.token = token

    def drop(self):
        self.token.drop(self.end())

    def append(self, q3baseview):
        self.end().append(q3baseview.token, q3baseview.end())

    def yieldCommands(self, commands=None):
        '''
        Yields Q3ConfigCommand objects for all commands in the order they appear.

        `commands` (list|tuple):
            Restrict the list to these command names.
        '''
        token = self.token
        while token is not None:
            token = token.findNext(isTWord, include_self=True)
            if token:
                token1 = token
                token = token.findNext(isCommandEnd)
                if token:
                    token = token.next
                if commands is None or token1.s in commands:
                    c = Q3ConfigCommand.view(token1)
                    yield c

    def yieldVariables(self, commands=('set', 'seta', 'sets', 'setu')):
        '''
        Yields Q3ConfigVariable objects for all variables in the order they appear.
        '''
        for c in self.yieldCommands(commands):
            if len(c) > 2:
                c.__class__ = Q3ConfigVariable # TODO
                yield c

    def yieldBindings(self):
        '''
        Yields Q3ConfigBinding objects for all bindings in the order they appear.
        '''
        for c in self.yieldCommands(('bind',)):
            if len(c) > 2:
                c.__class__ = Q3ConfigBinding # TODO
                yield c

class Q3Config(Q3BaseView):
    r"""
    Quake3 Configration parser.

    >>> s = '''\
    ... // Sample config
    ... bind ENTER    "ending quote missing
    ... seta unquoted unquoted/not-a-comment//a comment
    ... seta quoted   "quoted//also not a comment"
    ... seta name     Unnamed Player // Player name\
    ... '''
    >>> q3cfg   = Q3Config.from_string(s)
    >>> q3vars  = q3cfg.getVariables()
    >>> q3binds = q3cfg.getBindings()
    >>> q3vars['unquoted'].setValue('still_unquoted')
    >>> q3vars['quoted'].setValue('still_quoted')
    >>> q3vars['name'].setValue('My cool new Name')
    >>> q3vars['new'] = 'A new variable'
    >>> print(str(q3cfg))
    // Sample config
    bind ENTER    "ending quote missing"
    seta unquoted still_unquoted//a comment
    seta quoted   "still_quoted"
    seta name     "My cool new Name" // Player name
    seta new "A new variable"
    """

    @staticmethod
    def from_string(string):
        ''' Load configuration from string '''
        token_start = Q3Config.parse_string(string)
        return Q3Config(token_start)

    @staticmethod
    def from_file(filename, not_found_okay=False):
        ''' Load configuration from file '''
        token_start = None
        try:
            with open(filename, 'r') as fh:
                token_start = Q3Config.parse_string(fh.read(-1))
        except FileNotFoundError:
            if not_found_okay is False:
                raise
        c = Q3Config(token_start)
        c.file = filename
        return c

    def __init__(self, token):
        super(Q3Config, self).__init__(token)
        self.file = None

    def __iter__(self):
        return self.token.__iter__()

    @staticmethod
    def tokenize(string):
        ''' Yields bare (unlinked) tokens found in `string` '''
        for s in GRAMMAR.findall(string):
            if   s == '\n':           yield TNewline()
            elif s[0] == '"':         yield TQuoted(s[1:].rstrip('"'))
            elif s.isspace():         yield TWhitespace(s)
            elif s.startswith('//'):  yield TComment(s[2:])
            elif s == ';':            yield TSemicolon()
            else:                     yield TWord(s)

    @staticmethod
    def parse_string(string):
        ''' Parses the config as string '''
        root = last = TEmpty()
        for t in Q3Config.tokenize(string):
            last = last.append(t)
        return root

    def getBindings(self):
        '''
        Return a Q3ConfigBindings dict-like object of key bindings.
        '''
        return Q3ConfigBindings(self)

    def getVariables(self, commands=('set', 'seta', 'sets', 'setu')):
        '''
        Return a Q3ConfigVariables dict-like object of variables.
        '''
        return Q3ConfigVariables(self, commands)

    def prepend(self, token):
        raise NotImplementedError #TODO
        if not self.token:
            self.token = token
        else:
            self.token

    def begin(self):
        ''' Return the first token of the configuration '''
        return self.anchor

    def end(self):
        ''' Return the last token of the configuration.  '''
        return self.token.last()

    def __str__(self):
        ''' Return the configuration as string '''
        return ''.join(map(str, self.token))

    def write(self, filename):
        ''' Write the config. '''
        filename = self.file if filename is None else filename
        if filename is None:
            raise Exception('No file name')
        with open(filename, 'w') as fh:
            fh.write(str(self))

class Q3ConfigCommand(Q3BaseView):
    '''
    A class that acts as a `view` on tokens.

    Every word (TWord,TQuoted) from `token_start` to a command delimiter
    (TNewline, TSemicolon, TComment) will be considered as part of the command.

    The words of the command can be accessed/modified by using the [] operator.

    Whitespaces (TWhitespace) between the words will be preserved.
    If a new word is added, a single Space (' ') will be used as delimiter.

    #>>> cmd = Q3ConfigCommand()
    #>>> cmd[:] = ['a','word']
    #...
    '''

    @staticmethod
    def view(token):
        return Q3ConfigCommand(token)

    @staticmethod
    def create(words, separator=' ', terminator=';'):
        root = last = TEmpty()
        for word in words:
            last = last.append(TWord(word)).append(TWhitespace(separator))
        last.drop() # Drop last whitespace
        return Q3ConfigCommand(root)

    def getCommand(self):
        ''' Return the command name (`self[0]`). '''
        return self[0]

    def setCommand(self, name):
        ''' Set the command name (`self[0]`). '''
        self[0] = name

    def getWordAt(self, idx):
        if not self.token:
            raise IndexError

        if idx < 0:
            return list(self.token.findIter(isTWord, isCommandEnd))[idx]

        t = self.token.findNext(isTWord, isCommandEnd, include_self=True)
        for i in range(idx):
            t = t.findNext(isTWord, isCommandEnd)
            if t is None: raise IndexError
        return t

    def getValueAt(self, idx):
        return self.getWordAt(idx).s

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            return [w.s for w in
                islice(self.token.findIter(isTWord, isCommandEnd),
                idx.start, idx.stop, idx.step)]
        return self.getValueAt(idx)

    def __setitem__(self, i, value):
        #print('call'); self.token.dump()
        self.token.assert_valid_links()
        if isinstance(i, slice):
            values = iter(value)
            twords = islice(self.token.findIter(isTWord, isCommandEnd), i.start, i.stop, i.step)
            while True:
                try:
                    val = None
                    val = next(values)
                    try:
                        tok = next(twords)
                        tok.s = val
                    except StopIteration:
                        tok = tok.append(TWhitespace(' ')).append(TWord(val))
                except StopIteration:
                    if val is None:
                        try:
                            #print('Token dump'); self.token.dump()
                            self.token.assert_valid_links()

                            t = next(twords)
                            end = t.findNext(isCommandEnd)
                            end = end.prev if end else t.last()
                            t.drop(end)
                        except StopIteration:
                            pass
                            #print(2)
                    else:
                        #print(33333333333333)
                        values = [val] + list(values)
                        foo = Q3ConfigCommand.create(values)
                        foo = foo.token
                        last = foo.last()
                        tok.append(foo, last)
                    break
        else:
            self.getWordAt(i).s = value

    def __len__(self):
        return 1 + len(list(self.token.findIter(isTWord, isCommandEnd)))

    def __str__(self):
        return self.token.strTo(isCommandEnd)

    def begin(self):
        pass

    def end(self):
        end = self.token.findNext(isCommandEnd)
        return end or self.token.last()

class Q3ConfigVariable(Q3ConfigCommand):
    '''
    Specialization of Q3ConfigCommand, introduces explicit getter/setter
    for the variable name and variable value.
    '''
    def getName(self):
        ''' Return the name of the variable '''
        return self[1]

    def setName(self, name):
        ''' Set the name of the variable '''
        self[1] = name

    def getValue(self):
        ''' Return the value of the variable '''
        # Join token + trailing word tokens on space:
        #   `seta foo bar baz` -> foo is "bar baz"
        return ' '.join(self[2:])

    def setValue(self, value):
        ''' Set the value of the variable '''
        # Set the value on the existing token (to preserve possible quoting) and
        # remove trailing tokens
        if value != self.getValue():
            self[2:] = [value]

class Q3ConfigVariables:
    def __init__(self, q3config, commands=('seta', 'setu', 'sets', 'set')):
        self.q3config  = q3config
        self.commands  = commands
        self.variables = {}
        self.load()

    def load(self):
        variables = {}
        for var in self.q3config.yieldVariables(self.commands):
            variables[var.getName().lower()] = var
        self.variables = variables

    def __getitem__(self, varname):
        return self.variables[varname.lower()]

    def __setitem__(self, k, v):
        if k in self.variables:
            var = self.variables[k]
        else:
            var_tok = Q3ConfigCommand.make(['seta', k, ''])
            var = Q3ConfigVariable(self.q3config, var_tok)
            self.q3config.end().ensure_token(TNewline).insert(var_tok)
            self.variables[k.lower()] = var

        var.setValue(v)

class Q3ConfigBinding(Q3ConfigCommand):
    def getKey(self):
        return self[1]

    def setKey(self, key):
        self[1] = key

    def unbind(self):
        pass

    def bind(self, key):
        pass

    def getArgs(self):
        return self[2:]

    def setArgs(self, values):
        self[2:] = values

class Q3ConfigBindings:
    def __init__(self, q3config):
        self.q3config = q3config
        bindings = {}
        for binding in self.q3config.yieldBindings():
            bindings[binding.getKey()] = binding
        self.bindings = bindings

    def __getitem__(self, k):
        return self.bindings[k]

    def __setitem__(self, k, v):
        if k in self.bindings:
            binding = self.bindings[k]
        else:
            bind = Q3ConfigCommand.make(['bind', k])
            binding = Q3ConfigBinding(self.q3config, bind)
            self.q3config.end().ensure_token(TNewline).insert(bind)
        binding.setArgs(v)


if __name__ == '__main__':
    import sys, os

    # ___________________________ Token Tests _________________________________
    t = TWord('word')
    assert str(t) == 'word'
    t = TWord('with spaces')
    assert str(t) == '"with spaces"'
    t = TQuoted('quoted')
    assert str(t) == '"quoted"'

    t0 = TWord('hello')
    t1 = TWord('world')
    t0.append(t1)
    assert t0.next == t1
    assert t1.prev == t0
    assert t0.next.prev == t0
    assert t1.prev.next == t1
    assert t0.strTo() == 'helloworld'

    t1.drop()
    assert t0.next == None
    assert t1.prev == None
    assert t1.next == None
    assert t0.strTo() == 'hello'

    t1.prepend(t0)
    assert t0.next == t1
    assert t1.prev == t0
    assert t0.next.prev == t0
    assert t1.prev.next == t1
    assert t0.strTo() == 'helloworld'

    # ______________________ Q3ConfigCommand Tests ____________________________
    cmd = Q3ConfigCommand.create([])
    assert str(cmd) == ''
    cmd = Q3ConfigCommand.create(['command', 'with spaces'])
    assert str(cmd) == 'command "with spaces"'
    cmd[0] = 'arg1'
    assert str(cmd) == 'arg1 "with spaces"'
    cmd[0] = 'arg one'
    assert str(cmd) == '"arg one" "with spaces"'
    cmd[:] = []
    assert str(cmd) == ''

    class SubscriptableTester:
        ''' Tests if a List-like object behaves like a list '''
        def __init__(self, pyList, subscriptable):
            self.pyList = pyList
            self.subscriptable = subscriptable

        def __assert_equal(self):
            prevPyList        = list(self.pyList)
            prevSubscriptable = list(self.subscriptable)
            if prevPyList != prevSubscriptable:
                raise AssertionError('Lists did not match before the test')
            return prevPyList

        def __getitem__(self, key):
            prevPyList = self.__assert_equal()
            having   = self.subscriptable[key]
            expected = self.pyList[key]
            if having != expected:
                print('Having:  ', having)
                print('Expected:', expected)
                print('List is: ', prevPyList)
                raise AssertionError

        def __setitem__(self, key, value):
            prevPyList = self.__assert_equal()
            self.pyList[key]        = value
            self.subscriptable[key] = value
            having   = list(self.subscriptable)
            expected = list(self.pyList)
            if having != expected:
                print('Having:  ', having)
                print('Expected:', expected)
                print('Before:  ', prevPyList)
                raise AssertionError

    test = SubscriptableTester(['foo'], Q3ConfigCommand.create(['foo']))
    # __getitem__
    test[0]
    test[:]
    test[0:0]
    test[0:1]
    test[:] = ['foo','bar','baz']
    test[:]
    test[0:]
    test[:0]
    test[1:]
    test[:1]
    test[0:1]
    test[0:2]
    test[1:2]
    test[2:2]
    test[:9]
    test[9:]
    test[-1]
    test[-2]
    test[-3]
    #test[-1:0]
    #test[-2:0]
    # __setitem__
    test[0:] = ['zero', 'one', 'two']
    test[1:] = ['two', 'three', 'four']
    test[2:] = ['three']
    test[:1] = ['meh']
    test[:] = ['zero','one','two','three']
    test[1:2] = ['foo', 'bar', 'baz']
    test[-1] = 'bar'
    # TODO [:] = []

    #bindings  = cfg.getBindings()
    #bindings['F']    = ['set','my','foo bar']

    # _________________________ Q3Config Tests ________________________________
    config_test = '''
    // Test configuration
    seta var0 value
    seta var1 "value with spaces"
    '''

    def assert_strequal(a, b):
        ai, bi, l, i, EOF = iter(a), iter(b), 1, 0, False
        while not EOF:
            i += 1
            try:    ac = next(ai)
            except: ac = 'EOF'; EOF = True
            try:    bc = next(bi)
            except: bc = 'EOF'; EOF = True
            if ac == '\n': l += 1; i = 0
            if (ac != bc):
                print('a:\n', a, '\nb:\n', b)
                raise AssertionError('%r != %r on line %d:%d' % (ac, bc, l, i))

    cfg = Q3Config.from_string(config_test)
    assert_strequal(str(cfg), config_test)

    var0 = var1 = None
    for cmd in cfg.yieldCommands():
        if cmd[0] == 'seta':
            if cmd[1] == 'var0':
                var0 = cmd
            elif cmd[1] == 'var1':
                var1 = cmd

    var0[2], var1[2] = var1[2], var0[2]
    print(cfg)
    var0.drop()
    var1.drop()
    print(cfg)

    var2 = Q3ConfigCommand.create(['foo', 'bar'])
    cfg.append(var2)
    print(cfg)

    # _________________________________________________________________________
    cfg = Q3Config.from_file('/tmp/test.cfg')
    print('vars?')
    for v in cfg.yieldVariables():
        print(v)

    # ________________ Test on a real file (if available) _____________________
    f = os.path.join(os.path.expanduser('~'), '.openarena', 'baseoa', 'q3config.cfg')
    if os.path.isfile(f):
        content = open(f, 'r').read(-1)
        print('Loading', f)
        cfg = Q3Config.from_file(f)
        print('Checking', f)
        assert content == str(cfg)

    # _________________________ All tests passed ______________________________
    print('All tests passed')
    sys.exit(0)

    # TODO
    import sys, os, doctest
    doctest.testmod()

