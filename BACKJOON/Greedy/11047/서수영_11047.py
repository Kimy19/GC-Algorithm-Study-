#N,K,A 입력받아 저장
N, K = map(int, input().split(' '))
A = []

for i in range(N):
    A.append(int(input()))

#제일 큰 동전부터 나누면서 몫을 저장
result = 0
for i in reversed(A):
    result += (K//i)
    K %= i
    if K == 0:
        break

print(result)
