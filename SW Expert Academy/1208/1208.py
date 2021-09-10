import sys

sys.stdin = open("input.txt", "r")

for test_case in range(1, 10+1):

    n = int(input())
    box = list(input().strip().split(' '))
    for i in range(0, len(box)):
        box[i] = int(box[i])

    for i in range(0, n):
        box[box.index(max(box))] -= 1
        box[box.index(min(box))] += 1

    result = max(box) - min(box)
    print("#{} {}".format(test_case, result))
