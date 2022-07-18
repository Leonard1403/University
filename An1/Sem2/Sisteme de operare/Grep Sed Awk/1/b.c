#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>

int main()
{
		int pipefd[2];
		//pipefd[0] - read
		//pipefd[1] - write
		pipe(pipefd);
		int pid = fork();
		if(pid == 0){
				close(pipefd[0]);
				int fifo = open("fifo",O_RDONLY);
				int nr;
				int sum = 0;
				//printf("Cifrele citite din fifo sunt:");
				
				while(read(fifo,&nr,sizeof(int)))
				{
					//printf("%d ",nr);
					sum = sum + nr;		
				}

				write(pipefd[1],&sum,sizeof(int));
				close(pipefd[1]);
				exit(0);
		}
		else{
			close(pipefd[1]);
			int sum;
			read(pipefd[0],&sum,sizeof(int));
			printf("Suma este: %d", sum);
			close(pipefd[0]);
		}
		wait(0);
}
