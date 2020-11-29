
all: parse

CC=./AFL/afl-gcc -O0 -no-pie -fno-pic -g  -fno-stack-protector -m32 

parse: parse.c paulslib.c 
	${CC} $^ -o $@ -lm

clean:
	rm -f parse
