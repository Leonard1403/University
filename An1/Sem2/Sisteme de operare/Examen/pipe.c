#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main()
{
	//printf("Procesul actual: %d\nProcestul parinte: %d\n", getpid(),getppid());
	int i;
	for(i=0;i<4;i++)
	{
		if(fork() && i%2 == 1)
				break;
		printf("i: %d\n",i);
		printf("Procesul actual: %d\nProcesul parinte: %d\n",getpid(),getppid());
		printf("\n");
		//if(fork() && i%2 == 1){
		//	break;
		//}
	}
	return 0;
}
