#include <stdio.h>
#include <stdlib.h>

char gi[]="/bin/sh";
void gitf()
{	

	asm("pop %rdi;ret;");
	asm("pop %r13;ret;pop %r14;ret;pop %r15;ret;");
	asm("mov %r13,%rax;mov %r14,%rsi;mov %r15,%rdx;");
	asm("syscall;");

}


void vuln()
{	
	char buf[20];
	puts("input what do you want");
	read(0,buf,0x400);
}


int main()
{
	puts("no shell here");
	setbuf(stdout,NULL);
	setbuf(stdin,NULL);
	vuln();
	return 0;
}
