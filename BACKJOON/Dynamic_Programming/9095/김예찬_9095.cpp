#include<stdio.h>
int main()
{
	int n;
	int dp[11];
	int temp;
	dp[1] = 1;
	dp[2] = 2;
	dp[3] = 4;
	for (int i = 4; i <= 10; i++)
	{
		dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
	}
	
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
			scanf("%d", &temp);
			printf("%d\n", dp[temp]);
	}
	return 0;
 }
