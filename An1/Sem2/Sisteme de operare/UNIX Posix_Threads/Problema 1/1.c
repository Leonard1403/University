/*Scrieti un program C care primeste ca si argumente in linia de comanda oricate fisiere. Fiecare fisier va cantine doua numere intregi a inter 1 si 100 si b intre 1000 si 100000.
 * Prgramul va avea n variabile globale, n find numarul de fisiere date ca argument in linia de comanda. Programu va crea cate doua thread-uri x si y pentru fiecare fisier primit
 * ca argument, Fiecare pereche de thread-uri x si y va primi ca argument un fisier dat ca argument, thread-ul x va citi numarul a si b din fisier si va adauga valoarea lui a la
 * variabila globala asociata acestuia pana cand variabila globala va depasi valoarea lui b, moment in care x va trimite un semnal lui y si y va afisa pe ecran valoarea variabilei
 * globale*/

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int* var;
typedef struct
{
        int index;
        char* nume_fisier;
}pereche;

pthread_mutex_t m;
pthread_cond_t c;

void* fx(void *px)
{
        char* fisier = (*(pereche*)px).nume_fisier;
        int i = (*(pereche*)px).index;
        FILE* fd = fopen(fisier, "r");
        int a=0,b=0;
        fscanf(fd, "%d %d", &a, &b);
        fclose(fd);
        int s=0;
        while(s<=b)
        {
                pthread_mutex_lock(&m);
                var[i]+=a;
                if(var[i]>b)
                {
                        printf("Thread-ul x = %d, var[%d] = %d > %d\n", i, i, var[i], b);
                        pthread_cond_signal(&c);
                }
                pthread_mutex_unlock(&m);
                s+=a;
        }
        return NULL;
}
void* fy(void *py)
{
        char* fisier = (*(pereche*)py).nume_fisier;
        int i = (*(pereche*)py).index;
        FILE* fd = fopen(fisier, "r");
        int a=0,b=0;
        fscanf(fd, "%d %d", &a, &b);
        fclose(fd);
        pthread_mutex_lock(&m);
        while(var[i]<=b)
        {
                pthread_cond_wait(&c, &m);
        }
        printf("Variabila cu indicele %d are valoarea %d(multiplu de %d)\n", i, var[i], a);
        pthread_mutex_unlock(&m);
        free(py);
        return NULL;
}
int main(int argc, char** argv)
{
        var = (int*)malloc((argc-1)*sizeof(int));
        pthread_t *x = malloc((argc-1)*sizeof(pthread_t));
        pthread_t *y = malloc((argc-1)*sizeof(pthread_t));
        pthread_mutex_init(&m, NULL);
        pthread_cond_init(&c, NULL);
        int i;
        for(i = 0; i < argc-1; i++)
        {
                pereche* arg = (pereche*)malloc(sizeof(pereche));
                arg->index = i;
                arg->nume_fisier = argv[i+1];
                var[i] = 0;
                pthread_create(&x[i], NULL, fx, (void*)arg);
                pthread_create(&y[i], NULL, fy, (void*)arg);
        }
        for(i = 0; i < argc-1; i++)
        {
                pthread_join(x[i],NULL);
                pthread_join(y[i], NULL);
        }
        pthread_mutex_destroy(&m);
        pthread_cond_destroy(&c);
        free(x);
        free(y);
        free(var);
        return 0;
}
