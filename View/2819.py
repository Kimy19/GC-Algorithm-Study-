 def dfs(number, x, y):
    if len(number) == 7:
        result.add(number)
        return
      
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(number + maps[nx][ny], nx, ny)

    return


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for tc in range(1, 1 + int(input())):
    maps = [input().split() for _ in range(4)]

    result = set()
    for i in range(4):
        for j in range(4):
            dfs('', i, j)
    print('#{} {}'.format(tc, len(result)))
