count = int(input())

def modified_fibo(x):
    if x==1: return 1
    if x==2: return 2
    if x==3: return 4
    return modified_fibo(x-1)+modified_fibo(x-2)+modified_fibo(x-3)

for i in range(count):
    N = int(input())
    print(modified_fibo(N))
