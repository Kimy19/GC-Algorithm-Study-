import sys

sys.stdin = open("input.txt", "r")
T = int(input())

for test_case in range(1, T+1):

    n = int(input())
    arr = list(input().split(" "))
    biggest = int(arr[0])

    for i in range(1, n):
        if (biggest * int(arr[i])) > (biggest + int(arr[i])):
            biggest = biggest*int(arr[i])
        else:
            biggest = biggest + int(arr[i])


    result = biggest

    print('#{} {}'.format(test_case, result))
