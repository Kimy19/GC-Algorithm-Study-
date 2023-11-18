
#include <stdio.h>


int map[100][100];
#define RIGHT 1
#define LEFT -1
#define DOWN 0



int route(int x,int y,int way)
{

	if(map[x][y] == 2)
		return (1);
	if(x == 99)
		return (0);
	if(map[x][y] == 1)
	{
		if(way == DOWN)
		{
			if(y+1 != 100 && map[x][y+1])
				return(route(x,y+1,RIGHT));
			else if(y-1 != -1 && map[x][y-1])
				return(route(x,y-1,LEFT));
			else
				return(route(x+1,y,DOWN));
		}
		if (way == RIGHT)
		{
			if(y+1 != 100 && map[x][y+1])
				return(route(x,y+1,RIGHT));
			else
				return(route(x+1,y,DOWN));
		}
		if (way == LEFT)
		{
			if(y-1 != -1 && map[x][y-1])
				return(route(x,y-1,LEFT));
			else
				return(route(x+1,y,DOWN));
		}
	}
	return (0);
}

int main(int argc, char** argv)
{
	int test_case;
	int T;

	//freopen("../input.txt", "r", stdin);
	while(scanf("%d",&T)!=EOF)
	{
		// printf("\n!!!!!!!!!!!!!%d\n",T);
		for(int i = 0; i< 100; i++)
		{
			for(int j = 0; j< 100; j++)
			{
				scanf("%d ",&map[i][j]);

				// printf("%d ",map[i][j]);
			}
		}
		for(int i = 0; i<100; i++)
		{
			if(map[0][i]==1)
			{
				if(route(0,i,DOWN))
					printf("#%d %d\n",T,i);
			}
		}
	}

	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}