#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/wait.h>

int main(int argc, char** argv){
    int pipefd[2];
    pipe(pipefd); 
    int pid = fork();
     if(pid==0){
        close(pipefd[0]);
        int fifo = open(argv[1], O_RDONLY);
        int nr = 0;
        int s = 0;
        while(read(fifo, &nr, sizeof(int))){
            s+=nr;
        }
        close(fifo);
        unlink(argv[1]);
        write(pipefd[1], &s, sizeof(int));
        close(pipefd[1]);
        exit(0);
    }
    close(pipefd[1]);
    int s=0;
    read(pipefd[0], &s, sizeof(int));
    printf("%d", s);
    close(pipefd[0]);
    wait(0);
    
}
