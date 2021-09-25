#include <stdio.h>

int dp[11];

int fdp(int n) {

	if (dp[n] != 0) {
		return dp[n];
	}
	else {
		dp[n] = fdp(n - 1) + fdp(n - 2) + fdp(n - 3);
		return dp[n];
	}
	
}

int main() {
	
	int t,n;

	scanf("%d", &t);

	dp[0] = 1;
	dp[1] = 2;
	dp[2] = 4;

	for (int i = 0; i < t; i++) {
		scanf("%d", &n);

		printf("%d\n", fdp(n-1));
	}
	
	

	return 0;
}
