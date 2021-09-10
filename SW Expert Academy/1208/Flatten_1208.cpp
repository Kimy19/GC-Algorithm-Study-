#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int execute_dump(int*);//dump하는 함수

int main()
{
	int dumpNum, height[100] = { 0 };
	int i, j,result;
	for (i = 0; i < 10; i++)
	{
		scanf("%d", &dumpNum);
		for (j = 0; j < 100; j++)
		{
			scanf("%d", &height[j]);
		}
		for (j = 0; j < dumpNum; j++)
		{
			result = execute_dump(height);
			if(result>1)
				continue;
			else
				break;
		}
		printf("#%d %d\n",i+1, result);
	}
	return 0;
}
int execute_dump(int* ptr_height)
{
	int i;
	int max, max_index, min, min_index;
	int sameMaxflag = 0, sameMinflag = 0;
	for (i = 0; i < 100; i++)
	{
		if (i == 0)
		{
			max = ptr_height[i];
			min = ptr_height[i];
			max_index = min_index = 0;
		}
		else if (ptr_height[i] > max)
		{
			max = ptr_height[i];
			max_index = i;
			sameMaxflag = 0;
		}
		else if (ptr_height[i] < min)
		{
			min = ptr_height[i];
			min_index = i;
			sameMinflag = 0;
		}
		else if (ptr_height[i] == max)
		{
			sameMaxflag = 1;
		}
		else if (ptr_height[i] == min)
		{
			sameMinflag = 1;
		}
	}
	if (max - min > 1)
	{
		ptr_height[max_index]--;
		ptr_height[min_index]++;
	}
	
	if (sameMaxflag&&sameMinflag)//min max둘다 같은값이 잇을때
			return max - min;
	
	else if (sameMaxflag || sameMinflag)//min max중 하나만 같은값이 있을때
			return max - min -1;

	else//같은값이 없을때
			return max-min-2;
	

}
