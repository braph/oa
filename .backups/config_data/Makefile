all: q3keys.py commands.py variables.py

q3keys.py: .force
	./mk_q3keys.py > q3keys.py

commands.py: .force
	./mk_commands.py > commands.py

variables.py: .force
	cat values.py > variables.py
	./mk_variables.py >> variables.py

.force:
	-true
