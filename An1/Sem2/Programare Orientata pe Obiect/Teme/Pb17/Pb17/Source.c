#include <stdio.h>

int v[40015];

void ciur(int v[])
{
	// 0 = numar prim
	// 1 = numar neprim
	v[0] = 1;
	v[1] = 1;
	v[2] = 0;
	v[3] = 0;
	v[5] = 0;
	for (int i = 2; i <= 40000; i++)
	{
		if (v[i] == 0)
		{
			for (int j = i + i; j <= 40000; j = j + i)
			{
				v[j] = 1;
			}
		}
	}
}

int gcd(int a, int b)
{
	int r;
	while (b != 0)
	{
		r = a % b;
		a = b;
		b = r;
	}
	return a;
}
/*
int proprietate(int nr)
{
	int i = nr-1;
	printf("Numarul: %d\n", nr);
	for (i; i >= 2; i=i-1)
	{
		int val = gcd(i, nr);
		if (val == 1 && v[i] == 1)
		{
			printf("Sunt prime intre ele dar nr %d nu este prim", i);
			return 0;
		}
	}
	return 1;
}
*/

int main()
{
	
	int n = 8, i = 3, nr;
	ciur(v);
	nr = 0;
	int ok;
	while (nr < n)
	{
		ok = 1;
		int j;
		for (j = 2; j <= i - 1; j++)
		{
			if (gcd(i, j) == 1 && v[j] == 1)
			{
				ok = 0;
				break;
			}
		}
		if (ok == 1)
		{
			printf("%d ", i);
			nr++;
		}
		i++;
	}

	//printf("%d",gcd(25, 50));
	return 0;
}