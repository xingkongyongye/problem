#include <stdio.h>
#include <stdlib.h>

void shell()
{

	system("/bin/sh");
}

void vuln()
{	
	char buf[20];
	puts("what is your name?");
	read(0,buf,0x30);
	printf(buf);
	puts("what do you want to do?");
	printf("shell?%p",shell);
	read(0,buf,0x400);
}


int main()
{
	puts("Stop your stack overflow!");
	setbuf(stdout,NULL);
	setbuf(stdin,NULL);
	vuln();
	return 0;
}
