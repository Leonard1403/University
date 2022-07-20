#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <sys/stat.h>

int main(int argc, char** argv){
    int pipefd[2];
    pipe(pipefd);
    
    int pid = fork();
    if(pid == 0){
        close(pipefd[0]);
        int file = open(argv[1], O_RDONLY);
        int n=0;
        scanf("%d", &n);
        char ch;
        for(int i = 0; i<n; i++){
            read(file, &ch, sizeof(char));
        }
        write(pipefd[1], &ch, sizeof(char));
        close(pipefd[1]);
        close(file);
        exit(0);
    }
    close(pipefd[1]);
    char ch;
    read(pipefd[0], &ch, sizeof(char));
    close(pipefd[0]);
    if(ch>='0' && ch <= '9'){
        printf("numar");
    }else if((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')){
        printf("litera");
    }else{
        printf("other");
    }
    mkfifo(argv[2], 0600);
    int fifo = open(argv[2], O_WRONLY);
    write(fifo, &ch, sizeof(char));
    wait(0);
}   
