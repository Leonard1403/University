#include <stdio.h>

int main(int argc, char** argv){
	int pipefd[2];
	pipe(pipefd);
	//pipefd[0] - read
	//pipefd[1] - write

	int pid1 = fork();
	if(pid1==0)
	{
		close(pipefd[0]);
		char file[200];
		char cr;
		printf("Name file: ");
		scanf("%s",file);

		int number;
		printf("Number: ");
		scanf("%d",&number);

		int fd = open(file,O_RDONLY);
		while(read(fd,&cr,sizeof(char)) && number > 0)
		{
			n--;
		}
		write(pipefd[1],&cr,sizeof(char));

		close(pipefd[1]);
		exit(0);
	}
	wait(0);

	int pid2 = fork();
	if(pid2==0)
	{
		close(pipefd[1]);
		char cr;
		read(pipefd[0],&cr,sizeof(char));
		if((cr >= 'a' && cr <= 'b') && (cr <= 'A' && cr>= 'B'))
			printf("litera\n");
		else if(cr >='0' && cr<='9')

		close(pipefd[0]);
		exit(0);
	}
	wait(0);

	return 0;
}
