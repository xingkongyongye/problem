#include <stdio.h>
#include <stdlib.h>

void gift()
{	

	puts("there is something");
	system("emmm,guess what");
	asm("push 0x3024");
}

void vuln()
{	
	char buf[20];
	puts("input your sh");
	read(0,buf,0x30);
}


int main()
{
	puts("this problem is easy.Just no sh");
	setbuf(stdout,NULL);
	setbuf(stdin,NULL);
	vuln();
	return 0;
}
