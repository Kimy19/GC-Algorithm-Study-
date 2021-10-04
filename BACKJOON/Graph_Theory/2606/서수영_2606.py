N = int(input())
graph = [[] for _ in range(N+1)]

#주어진 쌍들로 연결된 그래프 생성
rela = int(input())
for i in range(rela):
    x, y = map(int, input().split(' '))
    graph[x].append(y)
    graph[y].append(x)

#dfs 탐색
visited = []
def dfs(v):
    visited.append(v)
    for i in graph[v]:
        if not i in visited:
            dfs(i)
    return len(visited)

#1은 제외
result = dfs(1) - 1

print('{}'.format(result))
