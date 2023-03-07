#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
  int c, l;
  struct sockaddr_in server;
  
  c = socket(AF_INET, SOCK_DGRAM, 0);
  if (c < 0) {
    printf("Eroare la crearea socketului client\n");
    return 1;
  }
  
  memset(&server, 0, sizeof(server));
  server.sin_port = htons(atoi(argv[2]));
  server.sin_family = AF_INET;
  server.sin_addr.s_addr = inet_addr(argv[1]);

  printf("Ip: %s si port %s\n",argv[1], argv[2]); 
  
  l = sizeof(server);

  //uint16_t a,b, suma;
  //char sir[100];
  //scanf("%hu",&a);
  //a = htons(a);
  //fgets(sir,sizeof(sir),stdin);
  //memset(sir,0,100);
  //memset(sir,0,strlen(sir));
  //sendto(c, &a, sizeof(a), 0, (struct sockaddr *) &server, sizeof(server));
  //recvfrom(c, &suma, sizeof(suma), 0, (struct sockaddr *) &server, &l);
  //suma = ntohs(suma);
  
  char msg[100];
  memset(msg, 0, 100);
  printf("Sirul: ");
  fgets(msg, sizeof(msg), stdin);
  sendto(c, msg, sizeof(msg), 0, (struct sockaddr*) &server, sizeof(server));

  //int a;
  //scanf("%d", &a);
  //a = htonl(a);
  //sendto(c, &a, sizeof(a), 0, (struct sockaddr*) &server, sizeof(server));
  
  int port;
  recvfrom(c, &port, sizeof(port), 0, (struct sockaddr*) &server, &l);
  port = ntohl(port);
  printf("Port: %d \n", port);
  
  int suma1;
  recvfrom(c, &suma1, sizeof(suma1), 0, (struct sockaddr*) &server, &l); 
  printf("Suma: %d \n", suma1); 
  
  //close(c);
  
  printf("Client nou\n");
 
  //c = socket(AF_INET, SOCK_DGRAM, 0);
  //if(c<0)
  //{
  //   printf("Eroare\n");
  //   return 1;
  //}

  memset(&server, 0, sizeof(server));
  server.sin_port = htons(port);
  server.sin_family = AF_INET;
  server.sin_addr.s_addr = inet_addr(argv[1]);

  int suma = 0;
  recvfrom(c,&suma, sizeof(suma), 0, (struct sockaddr*) &server, &l);
  suma = ntohl(suma);
  printf("Suma primtia: %d", suma);

  close(c);  
}
