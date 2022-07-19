#include <stdio.h>
#include <string.h>
// declaram functiile care se vor implementa in .asm

char functia(char s1[], char s2[], int n);

//declaram 2 siruri globale
char rez[]="0";

int main()
{
    //char s1[100], s2[100], s3[100];
    int n , m;
    // declaram variabilele
    char s1[] = "abcd";
    char s2[] = "efgh";
    n = 4;

    m = functia(s1, s2, n);
    // n = strlen(rez);
    // rez[n] = '\0';
    printf("Rezultatul1: %s", rez);
    printf("\n");
    
    m = functia(s2, s1, n);
    // n = strlen(rez);
    // rez[n] = '\0';
    printf("Rezultatul2: %s", rez);
    printf("\n");
    //m = functia(s2, s1, n);
    //printf("Rezultatul: %s", rez2);
    //printf("\n");
    return 0;
}
