#include <stdio.h>
int main(void)
{
	int test_case;
	int T;
	int N, D;
	//freopen("input.txt", "r", stdin);

	setbuf(stdout, NULL);
	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d %d",&N, &D);

		int range = D * 2 + 1;
		int result = 0;
		result = N / range;
		if(N % range)
			result++;
		printf("#%d %d\n",test_case,result);



	}
	return 0; //정상종료시 반드시 0을 리턴해야 합니다.
}