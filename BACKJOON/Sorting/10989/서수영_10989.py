import sys
from collections import deque

#sys.stdin = open('input.txt', 'r')

N = int(input())
'''
arr = deque()

def binary_search(arr, value, start, end):
    middle_index = (start + end)//2

    if end-start <= 1 :
        if arr[start] > value:
            return start
        elif arr[end] < value:
            return end+1
        else:
            return end

    if arr[middle_index] < value:
        r = binary_search(arr, value, middle_index+1, end)
    elif arr[middle_index] > value:
        if middle_index == 0:
            return 0
        r = binary_search(arr, value, start, middle_index-1)
    elif arr[middle_index] == value:
        return middle_index

    else: return False
    return r


arr.append(int(input()))
buff = int(input())
if buff >= arr[0]:
    arr.append(buff)
else:
    arr.appendleft(buff)

for i in range(2, N):
    v = int(input())
    idx = binary_search(arr, v, 0, i-1)
    arr.insert(idx, v)

for i in range(N):
    print(arr.popleft())
'''
q = [0] * 10001

for i in range(N):
    v = int(sys.stdin.readline())
    q[v] += 1

for i in range(10001):
    if q[i] != 0:
        for j in range(q[i]):
            print(i)
