#include <stdio.h>

int gcd(int a, int b){
	while(a!=b){
		if(a>b) a = a - b;
		else b = b - a;
	}
	return a;
}
int main(int argc, char** argv){
		
		int a, b;
		printf("a = ");
		scanf("%d",&a);
		printf("b = ");
		scanf("%d",&b);
		
		return 0;
}
