
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <stdlib.h>
#include <fcntl.h>

int main(int argc,char** argv){
	int pipefd[2];
	pipe(pipefd);
	//pipefd[0] - read
	//pipefd[1] - write
	int fifo = open(argv[1],O_RDONLY);
	
	int pid1 = fork();
	if(pid1 == 0)
	{
		close(pipefd[0]);

		int nr;
		int s = 0;
		while(read(fifo,&nr,sizeof(int)))
		{
			s = s + nr;
		}
		write(pipefd[1],&s,sizeof(int));

		close(pipefd[1]);
		exit(0);
	}
	wait(0);
	
	int pid2 = fork();
	if(pid2 == 0)
	{
		close(pipefd[1]);

		int s;
		read(pipefd[0],&s,sizeof(int));
		printf("Suma: %d",s);

		close(pipefd[0]);
		exit(0);
	}
	wait(0);
	close(fifo);
	unlink(argv[1]);
	return 0;
}
