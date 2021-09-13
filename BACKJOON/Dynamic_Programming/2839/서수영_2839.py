N = float(input())
count = []

#x(0 ... N/3), y = -3/5x + N/5
for x in range(0, int(N/3)+1):
    y = -3*x + N

    if(x%1 == 0 and (y/5)%1 == 0):
        count.append(x+(y/5))

if len(count) != 0:
    print(int(min(count)))
else:
    print(-1)
