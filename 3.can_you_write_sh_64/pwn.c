#include <stdio.h>

char s[100];
void gitf()
{	
	asm("pop %rdi;ret");
	asm("pop %rsi;ret");
	asm("pop %rdx;ret");
	
}
void back_door()
{
	system("what fu*** it");
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
