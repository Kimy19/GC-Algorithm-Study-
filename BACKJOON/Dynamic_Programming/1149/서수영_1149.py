import sys

#sys.stdin = open('input.txt', 'r')

N = int(input())

cost_list = []


for i in range(N):
    cost_list.append(list(map(int, input().strip().split())))

for i in range(1, N):
    cost_list[i][0] += min(cost_list[i - 1][1], cost_list[i - 1][2])
    cost_list[i][1] += min(cost_list[i - 1][0], cost_list[i - 1][2])
    cost_list[i][2] += min(cost_list[i - 1][0], cost_list[i - 1][1])


print(min(cost_list[N-1]))
