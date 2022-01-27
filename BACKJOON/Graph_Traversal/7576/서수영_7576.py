import sys
from collections import deque
sys.setrecursionlimit(10**6)

#sys.stdin = open('input.txt', 'r')

M, N = map(int, input().split(' '))
graph = []
q = deque()
#graph = [[0 for i in range(M)] for j in range(N)]
for i in range(N):
    graph.append(list(map(int, input().strip().split(' '))))
#print(graph)

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i,j))
#print(q)

def bfs(start_q):

    days = 0

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]


    while(q):
        days += 1

        '''
        for k in range(N):
            print(graph[k])
        print('')
             '''
        oneday_count = len(q)

        for i in range(oneday_count):
            x, y = q.popleft()

            for i in range(4):
                cx = x + dx[i]
                cy = y + dy[i]

                if 0<= cx < N and 0<= cy <M:
                    if graph[cx][cy] == 0:
                        graph[cx][cy] = 1
                        q.append((cx, cy))
    return days -1

result = bfs(q)

for check in graph:
    if 0 in check:
        result = -1

print('{}'.format(result))
