#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char** argv){
    char ch;
    int fifo = open(argv[1], O_RDONLY);
    read(fifo, &ch, sizeof(char));
    close(fifo);
    unlink(argv[1]);
    printf("%d", ch);
}

