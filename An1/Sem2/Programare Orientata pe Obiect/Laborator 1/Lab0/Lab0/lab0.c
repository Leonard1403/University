#include <stdio.h>

int main()
{
	int n, s, nr;
	printf("n = ");
	scanf_s("%d", &n);
	s = 0;
	for (int i = 1; i <= n; i++)
	{
		printf("nr = ");
		scanf_s("%d", &nr);
		s = s + nr;
	}
	printf("Suma celor %d numere este: %d", n, s);
	return 0;
}