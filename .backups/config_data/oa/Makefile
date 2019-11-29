#
# Parse cvars from source/openarena console
#

OA_DIR ?= /tmp/OpenArena-gamecode-b7e01f4

all: source_vars.py cvardump.py

source_vars.py: .force
	./parse_source.py $(shell find $(OA_DIR) -iname '*.c') > source_vars.py

cvardump.py: cvardump.out .force
	./parse_cvardump.py > cvardump.py

cvardump.out:
	@echo 'Please run oa_cvardump.sh manually'
	exit 1

.force:

