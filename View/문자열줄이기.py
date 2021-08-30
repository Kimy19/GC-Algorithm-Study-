def solution(s):

    shortest = []
    r = int(len(s)/2)+1
    if r == 1:
        r = 2
    for i in range(1, r):
        length = i
        list_s = []
        flag = 0
        for j in range(0, len(s), i):
            list_s.append(s[j:j+i])
        for k in range(0, len(list_s) - 1):


            if( list_s[k] == list_s[k+1]):
                flag += 1
            else:
                length += len(list_s[k+1])

                if (flag != 0):

                    length += len(str(flag+1))

                    flag = 0
            if(k == len(list_s)-2 and flag != 0):
                length += len(str(flag+1))


        shortest.append(length)

    result = min(shortest)
    return result

s = "xxxxxxxxxxyyy"
print(solution(s))
