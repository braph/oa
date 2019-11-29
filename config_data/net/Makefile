#
# Descriptions of variables/commands taken from the internet
#

all: stupidctf.json joz3d.json quake3tweaks.json

stupidctf.json: .force
	./crawl_stupidctf.tk.py > stupidctf.json

joz3d.json: .force
	./crawl_joz3d.net.py > joz3d.json

quake3tweaks.json: .force
	./crawl_quake3tweaks.tripod.com.py > quake3tweaks.json

.force:
	@true
