#include <stdio.h>

int main()
{
	int tc, n;
	double d, k[2], s[2], time[2], t;

	scanf("%d", &tc);

	for (int i = 0; i < tc; i++) {
		scanf("%lf %d", &d, &n);

		time[0] = 0;
		time[1] = 0;

		for (int j = 0; j < n; j++) {
			scanf("%lf %lf", &k[j], &s[j]);
			time[j] = (d - k[j]) / s[j];
		}
		if (time[0] > time[1])
			t = time[0];
		else
			t = time[1];


		printf("#%d %-.7lf\n", i + 1, d / t);

	}

	return 0;
}
