from collections import deque
'''
import sys
sys.stdin = open('input.txt', 'r')
'''
N, M, V = map(int, input().split(' '))
start = V
#print(N, M, V)

graph = dict()
for i in range(1, N+1):
    graph[i] = []

for i in range(M):
    a, b = map(int, input().split(' '))
    graph[b].append(a)
    graph[b].sort()
    graph[a].append(b)
    graph[a].sort()

#print(graph)



def dfs(graph, start, visited=[]):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)

    return visited

def bfs(graph, start, visited=[]):
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited

graph_dfs = dfs(graph, V)
for i in graph_dfs:
    print(i, end=' ')
print('')

graph_bfs = bfs(graph, V)
for i in graph_bfs:
    print(i, end=' ')
