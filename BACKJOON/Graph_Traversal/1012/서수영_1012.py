import sys
from collections import deque

sys.setrecursionlimit(10**6)

sys.stdin = open('input.txt', 'r')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    queue.append((x, y))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<M and (nx, ny) not in queue and vegetable_map[nx][ny] == 1:
            dfs(nx, ny)

    return 0

T = int(input())

for i in range(T):
    queue = deque()
    cnt = 0
    #P(N, M)
    M, N, K = map(int, input().split(' '))

    vegetable_map = [[0 for _ in range(M)] for _ in range(N)]

    for j in range(K):
        y, x = map(int, input().split(' '))
        vegetable_map[x][y] = 1


    for j in range(N):
        for k in range(M):
            if (j,k) not in queue and vegetable_map[j][k] == 1:
                dfs(j, k)
                cnt += 1
    print(cnt)
