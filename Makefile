all: parser.rom

parser.rom: parser.tal helpers.tal
	uxnasm $< $@

run: parser.rom
	uxncli parser.rom

clean:
	rm -f parser.rom