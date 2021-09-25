#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int kg[5001];

int sugar(int n) {

	kg[5] = 1, kg[3] = 1;

	if (n < 3)
		return -1;
	
	if (kg[n] != 0) {
		return kg[n];
	}

	if (n % 5 == 0) {
		kg[n] = n / 5;
	}
	else if (n == 4 || n == 7) {
		return -1;
	}
	else {
		kg[n] = sugar(n - 3) + 1;
	}
	
	return kg[n];
}

int main() {

	int n, b;
	scanf("%d", &n);

	b = sugar(n);
	
	printf("%d", b);
	
	return 0;
}
