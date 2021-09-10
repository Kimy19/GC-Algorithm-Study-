n = 10
val = 1

arr = [[0 for i in range(n)] for j in range(n)]


def sly(a, start):
    t, k = 0, 0
    global val

    for t in range(start, start+a+1):
        arr[start][t] = val
        val += 1

    for k in range(start, start+a+1):
        arr[k][t+1] = val
        val += 1

    for t in range(start+a+1, start, -1):
        arr[k+1][t] = val
        val += 1

    for k in range(start+a+1, start, -1):
        arr[k][t-1] = val
        val += 1
'''
sly(2, 0)
sly(0,1)


sly(3, 0)
sly(1, 1)
'''

j=2
for i in range(0, int(n/2)):
    sly(n-j, i)
    j+=2

if (n%2 == 1): arr[int(n/2)][int(n/2)] = val

for i in range(n):
    print(arr[i])
