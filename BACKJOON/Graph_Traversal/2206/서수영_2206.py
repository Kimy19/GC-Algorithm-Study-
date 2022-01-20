import sys
from collections import deque

sys.setrecursionlimit(10*6)
sys.stdin = open('input.txt', 'r')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N, M = map(int, input().split())

graph = []
result_list = []
queue = deque()
graph_cost = [[[0]*2 for j in range(M)] for i in range(N)]

for i in range(N):
    graph.append(list(map(int, str(input().strip()))))

def BFS(x, y, z):
    graph_cost[x][y][z] = 1
    queue.append((x,y,z))

    while(1):
        x, y, z = queue.popleft()
        for d in range(4):
            cx = x + dx[d]
            cy = y + dy[d]

            if 0 <= cx < N and 0 <= cy < M:
                if graph[cx][cy] == 1 and z == 1:
                    graph_cost[cx][cy][z-1] = graph_cost[x][y][z] + 1
                    queue.append((cx, cy, z-1))
                if graph[cx][cy] == 0 and graph_cost[cx][cy][z] == 0:
                    graph_cost[cx][cy][z] = graph_cost[x][y][z] + 1
                    queue.append((cx, cy, z))

        if (x == N-1 and y == M-1):
            result = graph_cost[N-1][M-1][z]
            break

        if len(queue) == 0 :
            result = -1
            break

    return result

print((BFS(0, 0, 1)))


