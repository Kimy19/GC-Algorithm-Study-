#import sys


'''
#sys.stdin = open("input.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////
    T = int(input())

    arr = list(input().split(" "))

    result = 0

    for i in range(2, T - 2):
        buff = [int(arr[i - 2]), int(arr[i - 1]), int(arr[i]), int(arr[i + 1]), int(arr[i + 2])]
        buff.sort()

        if buff[4] == int(arr[i]):
            result += (int(buff[4]) - int(buff[3]))

    print('#{} {}'.format(test_case, result))
# ///////////////////////////////////////////////////////////////////////////////////
