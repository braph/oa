#
# Descriptions of variables/commands taken from the internet
#

all: stupidctf.py joz3d.py quake3tweaks.py

stupidctf.py: .force
	./crawl_stupidctf.tk.py > stupidctf.py

joz3d.py: .force
	./crawl_joz3d.net.py > joz3d.py

quake3tweaks.py: .force
	./crawl_quake3tweaks.tripod.com.py > quake3tweaks.py

.force:
	@true
