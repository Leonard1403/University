#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(int argc, char **argv) {
  	int pipefd[2];
	pipe(pipefd);
	//pipefd[0] - read
	//pipefd[1] - write
	int pid1 = fork();

	if(pid1==0)
	{
		//citim din primul copil
		close(pipefd[0]);
		int nr = 2129;
		write(pipefd[1],&nr,sizeof(int));
		printf("Primul copil\n");
		exit(0);
		close(pipefd[1]);
	}
	wait(0);
	int pid2 = fork();
	if(pid2==0){
		//citim din al-2lea copil
		close(pipefd[1]);
		int nr;
		read(pipefd[0],&nr,sizeof(int));
		printf("Al 2-lea copil\n");
		printf("nr: %d", nr);
		close(pipefd[0]);
		exit(0);
	}
	wait(0);
 	return 0;
}
