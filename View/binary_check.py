T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    result = "OFF"
    n, m = map(int, input().split())
	
    m_binary = m + 1
    n_binary = 2 ** n

    if m_binary % n_binary == 0:
        result = "ON"

    print('#{} {}'.format(test_case, result))
