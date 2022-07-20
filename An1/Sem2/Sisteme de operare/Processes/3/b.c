#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char** argv){
    
    int fifo = open(argv[1], O_RDONLY);
    int n=0;
    read(fifo, &n, sizeof(int));
    printf("%d", n);
    close(fifo);
    unlink(argv[1]);
}
