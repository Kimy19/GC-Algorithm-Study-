#include<stdio.h>
#include<stdlib.h>

int main()
{
	int Tc,N,M;
	int i, j;
	int binary[10000] = { 0, };
	int position = 0;
	scanf("%d", &Tc);
	for ( i = 0; i < Tc; i++)
	{
		scanf("%d %d", &N, &M);
		position = 0;
		while (1)
		{
			binary[position] = M % 2;   
			M  /= 2;             
			position++;    
			if (M == 0)   
				break;
		}
		for (j = position - 1; j >= 0; j--)
		{
			if(position<N)
			{
				printf("#%d OFF", i + 1);
				break;
			}
			if (j <= N - 1)
			{
				if (binary[j] != 1)
				{
					printf("#%d OFF",i+1);
					break;
				}

			}
			if(j==0)
				printf("#%d ON",i+1);
		}

		printf("\n");
	}

	return 0;
}
