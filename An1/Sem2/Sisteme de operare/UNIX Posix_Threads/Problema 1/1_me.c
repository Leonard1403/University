#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int* var;

pthread_mutex_t mut;
pthread_cond_t cond;

void* fx(void* var_x)
{
	char* nume_fisier = *(char*)var_x;
	return NULL;
}

void* fy(void* var_y)
{
	char* nume_fisier = *(char*)var_y;
	return NULL;
}

int main(int argc, char** argv){
	var = malloc((argc-1)*sizeof(int));
	pthread_t* tx;
	pthread_t* ty;
	pthread_mutex_init(&mut,NULL);
	pthread_cond_init(&cond,NULL);
	tx = (pthread_t*)malloc((argc-1)*sizeof(pthread_t));	
	ty = (pthread_t*)malloc((argc-1)*sizeof(pthread_t));
	for(int i=0;i<argc-1;i++)
	{
		pthread_create(&tx[i],NULL,fx,(void*) argv[i+1]);
		pthread_create(&ty[i],NULL,fy,(void*) argv[i+1]);
	}

	for(int i=0;i<argc-1;i++)
	{
		pthread_join(&tx[i],NULL);
		pthread_join(&ty[i],NULL);
	}
	pthread_mutex_destroy(&mut);
	pthread_cond_destroy(&cond);
	free(tx);
	free(ty);
	free(var);
	return 0;
}
