#include <stdio.h>

int dp[1000001], a[3];

int main() {
	
	int x;

	scanf("%d", &x);

	dp[3] = 1, dp[2] = 1;
	
		for (int i = 4; i <= x; i++) {
			a[0] = 1000001;
			a[1] = 1000001;
			a[2] = 1000001;
			if (i % 3 == 0) {
				a[0] = dp[i / 3] + 1;
			}
			if (i % 2 == 0) {
				a[1] = dp[i / 2] + 1;
			}

			a[2] = dp[i - 1] + 1;

			int min = 1000001;
			for (int j = 0; j < 3; j++) {
				if (min > a[j])
					min = a[j];
			}
			dp[i] = min;
		}
		printf("%d",dp[x]);
		
	
	

	return 0;
}
