import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

arr = []
for i in range(N):
    buff_age, buff_name = map(str, input().split(' '))
    buff = (int(buff_age), buff_name)
    arr.append(buff)

arr = sorted(arr, key=lambda x:(x[0]))

for i in range(N):
    print('{} {}'.format(arr[i][0], arr[i][1]))
