PYTHONVERSION :=2.7.5
PYTHONSMALLVERSION=2.7
CROSS :=
CC := $(CROSS)gcc
CXX := $(CROSS)g++
#INSTALL := $(shell ginstall --help >/dev/null 2>&1 && echo g)install
CFLAGS := -pthread -fno-strict-aliasing -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions --param=ssp-buffer-size=4 -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -DNDEBUG -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions --param=ssp-buffer-size=4 -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -I$(OPENSHIFT_DATA_DIR)Python-$(PYTHONVERSION) -I$(OPENSHIFT_DATA_DIR)Python-$(PYTHONVERSION)/Include
CXXFLAGS := -pthread -shared -Wl,-z,relro -L/usr/lib64 -L$(OPENSHIFT_DATA_DIR)Python-$(PYTHONVERSION) -lpython$(PYTHONSMALLVERSION)

.PHONY: all check clean

all: texcaller_wrap.o _texcaller.so

texcaller_wrap.o: texcaller_wrap.cxx
	$(CC) $(CFLAGS) -c texcaller_wrap.cxx -o texcaller_wrap.o

_texcaller.so: texcaller_wrap.o
	$(CXX) $(CXXFLAGS) texcaller_wrap.o -o _texcaller.so

clean:
	rm -f texcaller_wrap.o
	rm -f _texcaller.so
