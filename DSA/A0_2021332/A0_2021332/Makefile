CC = gcc #gcc compiler
ASM = nasm #nasm compiler
N = "asm" #output file name
make:
	${ASM} main.asm -felf64 -o ${N} && ${CC} asm
	@echo "Success"
clear:
	rm a.out asm