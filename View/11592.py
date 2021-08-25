
import sys

sys.stdin = open("input.txt", "r")
T = int(input())

for test_case in range(1, T+1):
    D, N = map(int, input().split())
    cruse_time = []
    k, s = 0, 0
    for i in range(0, N):
        k, s = map(int, input().split())
        #D = s*X + k, X = (D-k)/s
        #cruse: D = cruse_time*X( X = (D-k)/s ), cruse_time = D/((D-k)/s) = D*s / D-k
        cruse_time.append((D*s)/(D-k))

    result = min(cruse_time)
    print('#{} {}'.format(test_case, result))

