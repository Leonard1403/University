#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main(int argc,char **argv){
	mkfifo(argv[1],0600);	   
	int fd = open(argv[1],O_WRONLY);

	/*
	char s[200];
	strcpy(s,argv[2]);
	s[strlen(argv[2])] = 0;
	*/
	printf("Lungimea mesajului scrisa in linia de comanda este de: %ld\n", strlen(argv[2]));
	write(fd,argv[2],sizeof(argv[2]));
	close(fd);
	
	unlink(argv[1]);
	return 0;
}

