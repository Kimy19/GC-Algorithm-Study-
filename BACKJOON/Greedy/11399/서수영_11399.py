#N과 P 입력 받아 저장
N = int(input())
P = list((input().split(' ')))

#P 오름차순으로 정렬
for i in range(len(P)):
    P[i] = int(P[i])
P = sorted(P)

#한사람이 걸리는 시간은 자신과 나머지 사람이 자신이 인출하는 시간만큼 소요됨,
#i번쨰 사람에서 걸리는 시간은 Pi*(N-i+1), 0부터 N 까지 i에 대입하고 시간의 합을 구한다
result = 0

for i in range(N):
    result += P[i]*(N-i)

print(result)
