import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

arr = []
for i in range(N):
    buff = list(map(str, sys.stdin.readline().strip().split()))
    arr.append(buff)


arr_s = set(list(map(tuple, arr)))
arr = list(map(list, arr_s))

m = max(len(i) for i in arr)

for i in range(m):
    arr = sorted(arr, key=lambda x: (len(x[0]), x[i]))

a = sum(arr, [])
for i in a:
    print(i[:])
