
#변수 입력받아 저장
N = int(input())
meeting = []
buff = []

for i in range(N):
    buff = input().split(' ')
    buff[0], buff[1] = int(buff[0]), int(buff[1])
    meeting.append(buff)

#끝나는 시간 오름차순 정렬 후 같은거에 대해서 오름차순 정렬
meeting.sort(key=lambda x:(x[1], x[0]))

#N은 1 이상이므로 1개 이상의 회의가 열림, 가장 빨리 끝나는 회의는 무조건 열린다고 생각
result = 1
last_time = meeting[0][1]

for i in range(1, N):
    if meeting[i][0] >= last_time:
        last_time = meeting[i][1]
        result += 1


print(result)
