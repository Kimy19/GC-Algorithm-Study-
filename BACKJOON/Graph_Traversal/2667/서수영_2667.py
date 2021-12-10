import sys
from collections import deque
sys.setrecursionlimit(10**6)

#sys.stdin = open('input.txt', 'r')

result_arr = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque()
def dfs(x, y, count):
    queue.append((x, y))
    count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<N and (nx, ny) not in queue and house_map[nx][ny]:
            count = dfs(nx, ny, count)

    return count

N = int(input())

house_map = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    buff = input()
    for j in range(N):
        house_map[i][j] = int(buff[j])



#print(house_map)
buff = 0
cnt = 0
for i in range(N):
    for j in range(N):
        if house_map[i][j] and (i, j) not in queue:
            cnt += 1
            buff = dfs(i,j,0)
            result_arr.append(buff)

result_arr.sort()
print(cnt)
for i in result_arr:
    print(i)
