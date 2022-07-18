#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

pthread_cond_t c;

pthread_mutex_t m;

int x;

void * thread(void * arg)
{
  int i;
  for (i = 0; i < 100; i++)
  {
    pthread_mutex_lock(&m);
    x++;
    if (x % 5 == 0)
    {
	printf("Face cv?\n");
      pthread_cond_signal(&c);
    }
    pthread_mutex_unlock(&m);
  }
  return 0;
}

void * watcher(void * arg)
{
  pthread_mutex_lock(&m);
  while (x < 10000)
  {
	printf("Intram in asteptare\n");
        pthread_cond_wait(&c, &m);
 	printf("Da\n");
    /*
      unlock m
      w8 
      lock m
    */
  
    printf("x = %d\n", x);
    //pthread_mutex_unlock(&m);
  //  pthread_mutex_lock(&m);
  	//pthread_cond_wait(&c,&m);
  }
  
  pthread_mutex_unlock(&m);
  return 0;
}

int
main (int argc, char **argv)
{
  int n = 100;
  
  pthread_cond_init(&c, 0);
  
  pthread_mutex_init(&m, 0);

  pthread_t *t;
  
  t = malloc(n * sizeof(pthread_t));
  
  int i;
  
  pthread_t w;
  
  pthread_create(&w, 0, watcher, 0);
  
  for (i = 0; i < n; i++)
  {
    pthread_create(&t[i], 0 , thread, 0);
  }
  
  for (i = 0; i < n; i++)
  {
    pthread_join(t[i], 0);
  }

  printf("x ==== %d\n", x);

//  pthread_cond_signal(&c);

  pthread_join(w, 0);

  pthread_cond_destroy(&c);
  
  pthread_mutex_destroy(&m);
  
  free(t);
  
  return 0;
}

