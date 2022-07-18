#include <stdio.h>

int v[10015];

void ciur(int v[])
{
	// 0 = numar prim
	// 1 = numar neprim
	v[1] = 1;
	v[2] = 0;
	v[3] = 0;
	v[5] = 0;
	for (int i = 2; i <= 10000; i++)
	{
		if (v[i] == 0)
		{
			for (int j = i+i; j <= 10000; j = j + i)
			{
				v[j] = 1;
			}
		}
	}
}
int main()
{
	int n;
	printf("n: ");
	scanf_s("%d", &n);
	ciur(v);
	/*
	for (int i = 1; i <= 100; i++)
	{
		printf("v[%d] = %d\n", i, v[i]);
		if (v[i] == 0)
			printf("Numarul %d este prim\n", i);
		else
			printf("Numarul %d nu este prim\n", i);
	}
	*/
	int i = 1;
	while (n >= 1)
	{
		if (v[i] == 0)
		{
			n--;
			printf("%d ", i);
		}
		i++;
	}
	return 0;
}