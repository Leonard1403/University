#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc,char** argv){
	int pipefd[2];
	//pipefd[0] - read
	//pipefd[1] - write
	pipe(pipefd);
	int pid = fork();
	if(pid == 0){
		close(pipefd[0]);
		int fifo = open(argv[1], O_RDONLY);
		int nr = 0;
		int s = 0;
		while(read(fifo, &nr, sizeof(int))){
			s = s + nr;
		}
		close(fifo);
		unlink(argv[1]);
		write(pipefd[1],&s,sizeof(int));
		close(pipefd[1]);
		exit(0);
	}
	else{
		int suma;
		close(pipefd[1]);
		read(pipefd[0],&suma,sizeof(int));
		printf("Suma: %d", suma);
		close(pipefd[0]);	
	}
	wait(0);
}
