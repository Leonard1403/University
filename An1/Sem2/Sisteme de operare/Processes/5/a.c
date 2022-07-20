#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>

int main(int argc, char** argv){
    mkfifo(argv[1], 0600);
    int fifo = open(argv[1], O_WRONLY);
    int nr = 0;
    scanf("%d", &nr);
    int i = 0;
    for(i = 1; i<=nr; i++){
        if(nr%i==0){
            write(fifo, &i, sizeof(int));
        }
    }
}
