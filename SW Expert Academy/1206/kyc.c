
#include <stdio.h>

int main() {
	int box[1000];
	int result[10] = { 0 };
	int i, j, n, max2 = 0;
	int total = 0;
	for (int k = 0; k < 10; k++)
	{
		scanf("%d", &n);
		for (i = 0; i < n; i++)
		{
			scanf("%d", &box[i]);
		}
		for (i = 2; i < n-2; i++)
		{
			for (j = i - 2; j <= i + 2; j++)
			{
				if (i == j)
					continue;
				if (box[i] > box[j])
				{
					if (j == i - 2)
						max2 = box[j];
					if (box[j] > max2)
						max2 = box[j];
					if (j == i + 2)
						result[k] += box[i] - max2;
				}
				else
					break;

			}

		}
		
	}
	for (i = 0; i < 10; i++)
	{
		printf("#%d %d\n",i+1, result[i]);
	}
	return 0;
}
//WooWang good
