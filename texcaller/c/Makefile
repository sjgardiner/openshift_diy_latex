CROSS :=
AR := $(CROSS)ar
CC := $(CROSS)gcc
CXX := $(CROSS)g++
INSTALL := $(shell ginstall --help >/dev/null 2>&1 && echo g)install
CFLAGS := -O3 -ansi -pedantic -W -Wall -Werror

.PHONY: all check clean

all: libtexcaller.a
libtexcaller.a: texcaller.c texcaller.h
	$(CC) $(CFLAGS) -c -o texcaller.o texcaller.c
	rm -f libtexcaller.a
	$(AR) crs libtexcaller.a texcaller.o

check: all
	$(CC) $(CFLAGS) -I. -L. -o example example.c -ltexcaller
	./example
	$(CXX) $(CFLAGS) -I. -L. -o example_cxx example.cxx -ltexcaller
	./example_cxx

clean:
	rm -f texcaller.o libtexcaller.a
	rm -f example example_cxx
	rm -f texcaller.pc
