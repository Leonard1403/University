#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc,char** argv)
{
	mkfifo(argv[1],0600);
	int fd = open(argv[1],O_WRONLY);
	int nr;
	scanf("%d",&nr);
	for(int i=1;i<=nr;i++)
	{
		if(nr%i==0){
			write(fd, &i, sizeof(int));
		}
	}
}
