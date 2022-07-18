#include <stdio.h>
#include <stdlib.h>
#include<pthread.h>
int nr_pare;

typedef struct{
char* nume_fisier;
int n;
}ceva;

pthread_mutex_t m;

void* f(void* f_thread){
 char* nume = (*(ceva*)f_thread).nume_fisier;
 int numar = (*(ceva*)f_thread).n;
 FILE* fisier=fopen(nume,"r");
 int x, nr=0;
 while(fscanf(fisier, "%d", &x)!=EOF && nr<numar)
{
	if(x%2==0)
	{
		pthread_mutex_lock(&m);
		nr_pare+=x;
		pthread_mutex_unlock(&m);
		nr+=1;		
	}
		
}
  fclose(fisier);
  free(f_thread);
  return NULL;
}

int main (int argc, char **argv)
{
  pthread_t *t=malloc((argc-1)/2*sizeof(pthread_t));
  
  int i;
  pthread_mutex_init(&m,NULL);
  for(i=0; i<argc-1;i+=2)
{
   ceva *s = malloc(sizeof(ceva));
   s->nume_fisier = argv[i+1];
   s->n = atoi(argv[i+2]);
   pthread_create(&t[i/2],NULL,f,(void*) s);
     
}
for(i=0;i<argc-1;i+=2)
{
  pthread_join(t[i/2],NULL);
}
printf("%d\n", nr_pare);
free(t);
pthread_mutex_destroy(&m);
  return 0;
}

