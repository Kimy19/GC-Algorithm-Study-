#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int num, price[1000001];
long long total = 0;
int start = 0;

long long max_calculate();
int max_finder();

int main()
{
	int tc;
	int i, j;
	
	scanf("%d", &tc);
	for (j = 0; j < tc; j++)
	{
		scanf("%d", &num);
		
		for (i = 0; i < num; i++)
		{
			scanf("%d", &price[i]);
		}
		printf("#%d %lld\n",j+1,max_calculate());
		total = 0;
		start = 0;
	}
	return 0;
}
long long max_calculate()
{
	int i,max,max_position=0;

	while (start<num)
	{
		max_position = max_finder();
		max = price[max_position];
		for (i = start; i <= max_position; i++)
		{
			if (max_position == start)
			{
				start++;
				break;
			}
			else
			{
				if (i < max_position)
					total += max - price[i];
				else if (i == max_position)
				{
					start = max_position + 1;
					break;
				}
			}
		}
	}
	return total;
}
int max_finder()
{
	int i;
	int max,max_position;
	for (i = start; i < num; i++)
	{
		if (i == start)
		{
			max = price[i];
			max_position = i;
		}
		else if (price[i] >= max)
		{
			max = price[i];
			max_position = i;
		}
	}
	return max_position;
}
