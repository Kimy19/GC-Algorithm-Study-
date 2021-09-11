#include <stdio.h>

int num[11];

int cal(int num[], int n)
{
	int result = 0;

	for (int i = 0; i < n; i++) {
		if (result * num[i] > result + num[i]) {
			result *= num[i];
		}
		else
			result += num[i];
	}

	return result;
}

int main()
{
	int t, n, result;

	scanf("%d", &t);

	for (int i = 0; i < t; i++) {
		scanf("%d", &n);

		for (int j = 0; j < n; j++) {
			scanf("%d", &num[j]);
		}

		result = cal(num, n);
		printf("#%d %d\n", i + 1, result);

	}

	return 0;
}
