#
# Parse cvars from source/openarena console
#

all: gamecode source_vars.json cvarlist.json

source_vars.json: .force
	./from_gamedata_source.py $(shell find gamecode/code -iname '*.c') > source_vars.json

cvarlist.json: cvardump.out .force
	./from_cvarlist_dump.py > cvarlist.json

gamecode:
	git clone https://github.com/OpenArena/gamecode

cvardump.out:
	@echo 'Please run dump_cvars.sh manually'
	exit 1

.force:

