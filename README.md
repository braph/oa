**STILL BETA, DONT FORGET TO MAKE BACKUPS OF FILES YOU ARE EDITING!**

[Screenshot](http://pixelbanane.de/yafu/3928700682/oaconf.png)

Description
===========

OAConfigurator is a graphical user interface for editing Quake III based configuration files.

Current features:
- Lookup variable descriptions by hovering over a variable
- Syntax highlighting
- Validation of variable values
- Editor for colorizing strings
- It does __not mess up__ your existing configuration.
  The order of commands, comments, whitespace and even quoting style will be preserved.

Variable descriptions have been stolen from
- [joz3d.net](http://www.joz3d.net/html/q3console.html)
- [quake3tweaks.tripod.com](http://quake3tweaks.tripod.com/commands.html)
- [stupidctf.tk](http://stupidctf.tk/cvars)

Variable defaults, types and flags have been extracted from [Openarena Gamecode](https://github.com/OpenArena/gamecode).

Bugs / Todo
===========
- The failmod color palette is not 100% exact, since it was put together by using a color picker. (see [q3/q3colors.py](../blob/master/q3/q3colors.py))
  Bugging failgun about putting the hexcodes for the color palette online may help :)
- Special characters are not right yet [q3/q3specialchars.py](../blob/master/q3/q3specialchars.py)


Contribute
==========

- Did you spot an error?
- Are you missing a description of a variable?
- Want to fix my broken engrish?

Open an issue or a pull request.

You may also want to have a look at the [definitions file](../blob/master/config_data/oaconfigurator/make.py).
