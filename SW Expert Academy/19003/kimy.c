#include <stdio.h>
#include <stdlib.h>

int N,M;
int temp[100];
char *words[100];


int check_palindrom(char *str)
{
	char *front;
	char *back;

	front = str;
	while (*str)
		str++;
	back = str - 1;

	while (front < back)
	{
		if(*front != *back)
			return (0);
		front++;
		back--;
	}
	return (1);
}

int check_reverse(char *s1, char *s2)
{
	while(*s2)
		s2++;
	s2--;
	while(*s1)
	{
		if(*s1 != *s2)
			return (0);
		s1++;
		s2--;
	}
	return (1);
}

int get_max()
{
	int count = 0;
	int pair_count = 0;
	int max = 0;
	int palindrom_flag = 0;
	for(int i = 0; i<N; i++)
	{
		if(check_palindrom(words[i]))
			palindrom_flag = 1;
		else
			temp[count++] = i;
	}
	for (int i = 0; i< count-1; i++)
	{
		for (int j = i+1; j<count; j++)
		{
			if(check_reverse(words[temp[i]], words[temp[j]]))
			{
				pair_count++;
				break;
			}
		}
	}
	if(pair_count)
	max = (pair_count * 2)  * M; 
	if(palindrom_flag)
		max += M;
	return (max);
}
int main(void)
{
	int test_case;
	int T;
	char *temp;

	//freopen("../input.txt", "r", stdin);

	setbuf(stdout, NULL);
	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d %d",&N,&M);
		for (int i = 0; i < N; i++)
		{
			words[i] = (char*)malloc(sizeof(char)*(M+1));
			scanf("%s",words[i]);
			// printf("%s\n",words[i]);
		}
		printf("#%d %d\n",test_case, get_max());
		for(int i = 0; i < N; i++)
			free(words[i]);

	}
	return 0; //정상종료시 반드시 0을 리턴해야 합니다.
}
