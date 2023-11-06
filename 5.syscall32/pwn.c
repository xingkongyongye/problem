#include <stdio.h>
#include <stdlib.h>

char gi[]="/bin/sh";
void gitf()
{	

	asm("pop %eax;ret");
	asm("pop %ebx;ret");
	asm("pop %ecx;ret");
	asm("pop %edx;ret");
	asm("mov %ebx, 0; mov %eax, 1;int $0x80;");

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
