#include<stdio.h>
int dp[1000001];
int min(int a, int b)//작은 수 리턴하는 함수
{
	if (a < b)
		return a;
	else
		return b;
}
int main()
{
	int X;
	
	scanf("%d", &X);

	dp[1] = 0;
	for (int i = 2; i <= X; i++)//dp테이블 bottom up방식으로 채우기
	{
		if (i <= 3)
			dp[i] = 1;
		else
		{
			if (i % 3 == 0 && i % 2 != 0)//
				dp[i] = min(dp[i / 3], dp[i - 1])+1;
			else if (i % 3 != 0 && i % 2 == 0)
				dp[i] = min(dp[i / 2], dp[i - 1])+1;
			else if (i % 3 != 0 && i % 2 != 0)
				dp[i] = dp[i - 1]+1;
			else
				dp[i] = min(min(dp[i / 3], dp[i /2]),dp[i-1])+1;
		}


	}
	printf("%d", dp[X]);
	return 0;
}
