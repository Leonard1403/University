#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

typedef struct{
  int nr;
  int prev;
  int next;
  int index;
}triple;

int g=0;
pthread_mutex_t* m;

void* functie(void* da){
  triple trio = *(triple*)da;
  while(1){
    pthread_mutex_lock(&m[trio.index]);
    if(g>10000){
	pthread_mutex_unlock(&m[trio.next]);
        break;
    }
    g += trio.nr; 
    printf("g:%d %d\n", g, trio.index);
    if(g%2==0){
	printf("P:%d a deblocat pe %d\n", trio.index, trio.next);
    	pthread_mutex_unlock(&m[trio.next]);
    }
    else{
	printf("I:%d a deblocat pe %d\n", trio.index, trio.prev);
	pthread_mutex_unlock(&m[trio.prev]);
    }
  }
  return 0;
} 

int main (int argc, char **argv)
{
  int i;
  printf("Numarul de argumente este: %d", argc);
  triple* trio = (triple*)malloc((argc-1)/3*sizeof(triple));
  pthread_t* t;
  t = (pthread_t*)malloc((argc-1)/3*sizeof(pthread_t));
  m = (pthread_mutex_t*)malloc((argc-1)/3*sizeof(pthread_mutex_t));
  for(i=0; i<(argc-1)/3; i++)
  {
	trio[i].nr = atoi(argv[i*3+1]);
	trio[i].prev = atoi(argv[i*3+2]);
	trio[i].next = atoi(argv[i*3+3]);
	trio[i].index = i;
	pthread_mutex_init(&m[i], NULL);
	pthread_mutex_lock(&m[i]);
	pthread_create(&t[i], NULL, functie, (void*)&trio[i]);
  }

  pthread_mutex_unlock(&m[0]);

  for(i=0; i<(argc-1)/3; i++){
	pthread_join(t[i], NULL);

	pthread_mutex_destroy(&m[i]);
  }
  free(trio);

  return 0;
}
