SRCS = $(wildcard *.tal)
DEPS = $(SRCS:%.tal=%.d)

all: parser.rom

parser.rom: parser.tal
	uxnasm $< $@

%.d: %.tal
	./uxn-deps.py $<

run: parser.rom
	uxncli parser.rom

clean:
	rm -f *.rom* *.d

-include $(DEPS)