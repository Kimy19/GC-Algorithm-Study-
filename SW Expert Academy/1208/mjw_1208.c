#include <stdio.h>
int box[101];

int maxindex() {
	int max = 0;
	int index;

	for (int i = 0; i < 100; i++) {
		if (box[i] > max) {
			max = box[i];
			index = i;
		}
	}
	return index;
}

int minindex() {
	int min = 1001;
	int index;

	for (int i = 0; i < 100; i++) {
		if (box[i] < min) {
			min = box[i];
			index = i;
		}
	}
	return index;
}


int main()
{
	int dump, result;
	
	int max, min;

	for (int i = 0; i < 10; i++) {
		scanf("%d", &dump);
	
		for (int j = 0; j < 100; j++) {
			scanf("%d", &box[j]);
		}


		for (int k = 0; k < dump; k++) {
			max = maxindex();
			min = minindex();
			if (max == min || box[max] == (box[min] + 1))
				break;
			box[max]--;
			box[min]++;
			
		}
		max = maxindex();
		min = minindex();
		printf("#%d %d\n", i + 1, box[max]-box[min]);
	}

	return 0;
}
