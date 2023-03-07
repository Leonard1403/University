#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <unistd.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>
#include <stdlib.h>
#include <arpa/inet.h>

int suma_calc(char msg[]){
	int init_size = strlen(msg)-1;
        char delim[] = " ";

        char *ptr = strtok(msg, delim);
        int suma = 0;
        //printf("Numerele: ");
        while(ptr != NULL)
        {
                //printf(" %d ", atoi(ptr));
                suma = suma + atoi(ptr);
                ptr = strtok(NULL, delim);
        }
        //printf("Suma: %d \n", suma);
	free(ptr);
	return suma;
}

int main() {
  int s;
  struct sockaddr_in server, client;
  int c, l;
  
  s = socket(AF_INET, SOCK_DGRAM, 0);
  if (s < 0) {
    printf("Eroare la crearea socketului server\n");
    return 1;
  }
  
  memset(&server, 0, sizeof(server));
  server.sin_port = htons(1234);
  server.sin_family = AF_INET;
  server.sin_addr.s_addr = INADDR_ANY;
  
  if (bind(s, (struct sockaddr *) &server, sizeof(server)) < 0) {
    printf("Eroare la bind\n");
    return 1;
  }
 
  l = sizeof(client);
  memset(&client, 0, sizeof(client));

  printf("S-a deschis\n");  
  while(1){

        //uint16_t a, b, suma = 0;
	//char sir[100];
	//memset(sir,0,strlen(sir));
	//fgets(sir,sizeof(sir),stdin);
        //recvfrom(s, &a, sizeof(a), 0, (struct sockaddr *) &client, &l);
    	//printf("S-a conectat un client\n");
        //a = ntohs(a);
        //suma = htons(suma);
	//sendto(s, &suma, sizeof(suma), 0, (struct sockaddr *) &client, sizeof(client));
  	
	char msg[100];
	memset(msg, 0, 100);
	recvfrom(s, msg, sizeof(msg), 0, (struct sockaddr *) &client, &l);	
	printf("S-a primit: %s", msg);
	int port;
	printf("Port: ");
	scanf("%d", &port);
	port = htonl(port);
        sendto(s, &port, sizeof(port), 0, (struct sockaddr *) &client, sizeof(client));
	
	/*
	int init_size = strlen(msg)-1;
m	char delim[] = " ";

	char *ptr = strtok(msg, delim);
	int suma = 0;
	printf("Numerele: ");
	while(ptr != NULL)
	{
		printf(" %d ", atoi(ptr));
		suma = suma + atoi(ptr);
		ptr = strtok(NULL, delim);
	}
	printf("Suma: %d \n", suma);
	*/

	char *ip = inet_ntoa(server.sin_addr);
  	printf("IP: %s \n", ip);
	
	int suma = 1;
	suma = suma_calc(msg);
	sendto(s, &suma, sizeof(suma), 0, (struct sockaddr *) &client, sizeof(client));
	
	//suma = suma_calc(msg);
	//printf("Suma: %d\n", suma);
	//sendto(s, &suma, sizeof(suma), 0, (struct sockaddr *) &client, sizeof(client));

	//close(s);
	
	printf("Port schimbat \n");	
	int s1 = socket(AF_INET, SOCK_DGRAM, 0);
  	if (s1 < 0) {
   	   printf("Eroare la crearea socketului server\n");
    	   return 1;
 	}
	
	memset(&server, 0, sizeof(server));
  	server.sin_port = htons(port);
  	server.sin_family = AF_INET;
  	server.sin_addr.s_addr = INADDR_ANY;
  	
	if (bind(s1, (struct sockaddr *) &server, sizeof(server)) < 0) {
    	   printf("Eroare la bind\n");
    	   return 1;
  	}

	//printf("Ajuns\n");
	
	suma = htonl(suma);
	sendto(s1, &suma, sizeof(suma), 0, (struct sockaddr*) &client, sizeof(client));
	
  }
  close(s);
}

