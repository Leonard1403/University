#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char** argv)
{
	char s[100];
	char nr;
	scanf("%s",s);
	printf("Fisierul este: %s\n",s);
	int file = open(s,O_RDONLY);
	mkfifo("fifo",0600);
	int fifo = open("fifo",O_WRONLY);

	while(read(file,&nr,sizeof(char)))
	{
		if(nr>='0' && nr <= '9')
		{
			int number = nr-'0';
			write(fifo,&number,sizeof(int));
			printf("nr = %d\n", number);
		}
	}
	close(file);
	close(fifo);	
	return 0;
}
