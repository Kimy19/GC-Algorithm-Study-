#include<stdio.h>

int main()
{
	int weight;
	int dp[5000] ;

	for (int i = 0; i < 5000; i++)
	{
		dp[i] = -1;
	}
	scanf("%d", &weight);
	dp[3] = 1;
	dp[5] = 1;

	for (int i = 3; i <= weight; i++)
	{

		if (i >= 5)
		{
			if (dp[i - 5] != -1 && dp[i - 3] != -1)
			{
				if (dp[i - 5] < dp[i - 3])
					dp[i] = dp[i - 5] + 1;
				else
					dp[i] = dp[i - 3] + 1;
			}
			else if (dp[i - 5] != -1)
				dp[i] = dp[i - 5] + 1;
			else if (dp[i - 3] != -1)
				dp[i] = dp[i - 3] + 1;
		}
		else
			if(dp[i-3]!=-1)
				dp[i] = dp[i - 3] + 1;
	}
	printf("%d", dp[weight]);
}
