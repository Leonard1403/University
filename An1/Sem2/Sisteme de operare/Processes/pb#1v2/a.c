#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc,char** argv){
 	char nume_fisier[200], nr;
	int number;

	scanf("%s",nume_fisier);
	int fisier = open(nume_fisier,O_RDONLY);
	
	mkfifo("fifo",0600);
	int fifo = open(argv[1],O_WRONLY);

	while(read(fisier,&nr,sizeof(char)))
	{
		if(nr>='0' && nr <='9')
		{
			number = nr - '0';
			write(fifo,&number,sizeof(int));
		}
	}

	close(fisier);
	return 0;
}
