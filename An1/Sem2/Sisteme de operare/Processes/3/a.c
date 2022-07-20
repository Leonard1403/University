#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <sys/stat.h>

int main(int argc, char** argv){
    int pipefd[2];
    pipe(pipefd);
    int pid=fork();
    if(pid==0){
        close(pipefd[0]);
        int file = open(argv[1], O_RDONLY);
        int n = 0;
        scanf("%d", &n);
        char crt;
        while(read(file, &crt, sizeof(char)) && n>0){
            int nr=0;
            if(crt >= '0' && crt <= '9'){
                nr = crt - '0';
                n--;
            }
            //printf("%c", crt);
            write(pipefd[1], &nr, sizeof(int));
        }
        close(file);
        close(pipefd[1]);
        exit(0);
    }
    close(pipefd[1]);
    int nr=0;
    int s = 0;
    while(read(pipefd[0], &nr, sizeof(int))){
        if(nr%2==1){
            s+=nr;
        }
    }
    //printf("a%d", s);
    close(pipefd[0]);
    mkfifo(argv[2], 0600);
    int f = open(argv[2], O_WRONLY);
    write(f, &s, sizeof(int));
    wait(0);
}
