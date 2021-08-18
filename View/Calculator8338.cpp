#include<stdio.h>
#include<stdlib.h>
#include<string.h>


int main()
{
	int tc,N,num[9];
	int i, j;
	long long result = 0;
	scanf("%d", &tc);
	for (i = 0; i < tc; i++)
	{
		scanf("%d", &N);
		for (j = 0; j < N; j++)
		{
			scanf("%d", &num[j]);
		}
		
		for (j = 0; j < N; j++)//계산하는 두 수 중에 0이나 1이있으면 덧셈 아니면 곱셈
		{
			if (j == 0)
				result = num[j];
			else if (num[j] >1 && result>1)
			{
				result *=num[j];
			}
			else
			{
				result +=  num[j];
				
			}
			

		}
		printf("#%d %lld\n", i + 1, result);
		result = 0;
	}
	return 0;
}
