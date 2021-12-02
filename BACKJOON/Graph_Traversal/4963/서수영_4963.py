import sys
sys.setrecursionlimit(10 ** 6)

dx = [-1, -1, 0, 1, 1,  1,  0, -1]
dy = [ 0,  1, 1, 1, 0, -1, -1, -1]

def dfs(x,y):
    check_visited[x][y] = 1

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < h and 0<= ny < w:
            if world_map[nx][ny] == 1 and check_visited[nx][ny] == 0:
                check_visited[nx][ny] = 1
                dfs(nx, ny)

while(1):

    w, h = map(int, input().split(' '))
    if(w == h == 0): break

    world_map = [list(map(int, input().split(' '))) for _ in range(h)]
    check_visited = [[0]*w for _ in range(h)]
    count = 0


    for i in range(h):
        for j in range(w):
            if check_visited[i][j] == 0 and world_map[i][j] == 1:
                dfs(i, j)
                count += 1

    print(count)
