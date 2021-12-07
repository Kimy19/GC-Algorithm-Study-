import sys
from collections import deque
sys.setrecursionlimit(10**6)

#sys.stdin = open('input.txt', 'r')

way = deque()
def bfs(x, y):
    way.append((x, y))

    while(way):
        for i in range(len(way)):
            x, y = way.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<= nx < N and 0<= ny < M and check[nx][ny] == 0 and miro[nx][ny] == 1:
                    way.append((nx, ny))
                    check[nx][ny] = check[x][y] + 1

    return check[N-1][M-1]

# n,m 까지 경로의 길이 다 갱신하면서 저장

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split(' '))
check = [[0 for _ in range(M)] for _ in range(N)]
check[0][0] = 1
miro = [[] for _ in range(N)]


for i in range(N):
    arr = str(input())
    for j in range(M):
        miro[i].append(int(arr[j]))

result = bfs(0, 0)

print('{}'.format(result))
