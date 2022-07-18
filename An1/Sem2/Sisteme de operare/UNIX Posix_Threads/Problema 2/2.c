#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>

int var1 , var2;
//var1 = litere
//var2 = cifre
pthread_mutex_t m;
pthread_barrier_t b;

void* work(void* fisier){
	char* nume_fisier = (char*)fisier;
	printf("Fisierul este: %s\n", nume_fisier);
	FILE* fd;
	fd = fopen(nume_fisier,"r");
	char c;
	int letter , digit;
	letter = digit = 0;
	//pthread_barrier_wait(&b);
	pthread_mutex_lock(&m);
	while(fscanf(fd,"%c",&c)!=EOF){
		//printf("%c" , c);
		if(c>='0'&&c<='9')
			digit = digit + 1;
		if((c>='a'|| c>='A') && (c>='z' || c>='Z')){
			letter = letter + 1;
		}
	}
	printf("Nr de caractere: %d              Nr de cifre: %d\n", letter, digit);
	//printf("\n");
	pthread_mutex_unlock(&m);
	var1 = var1 + letter;
	var2 = var2 + digit;
	fclose(fd);
	//free(nume_fisier);
	//pthread_barrier_wait(&b);
	return 0;
}

int main(int argc, char** argv){
	pthread_t *th = malloc((argc-1)*sizeof(pthread_t));
	pthread_mutex_init(&m,NULL);
	pthread_barrier_init(&b,NULL,argc);
	printf("Nr argumente: %d\n", argc);
	int i;
	var1 = 0;
	var2 = 0;
	//char* nume_fisier;
	for(i=0;i<argc-1;i++)
	{
		//var1 = 0;
		//var2 = 0;
		//nume_fisier = (char*)malloc(sizeof(char));
		//nume_fisier = argv[i+1];
		pthread_create(&th[i], NULL , work,(void*)argv[i+1]);
		//free(nume_fisier);
	}
	//free(nume_fisier);
	//pthread_mutex_lock(&m);
	//pthread_barrier_wait(&b);
	//printf("TOTAL: Nr de litere: %d       Nr de cifre: %d\n",var1, var2);
	//pthread_mutex_unlock(&m);
	for(i = 0;i<argc-1;i++)
	{
			pthread_join(th[i],NULL);
	}
	printf("Total: nr de litere %d            nr de cifre:%d\n",var1 , var2);
	free(th);
	pthread_barrier_destroy(&b);
	pthread_mutex_destroy(&m);
	return 0;
}
