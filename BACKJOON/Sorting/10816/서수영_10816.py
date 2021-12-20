import sys

#sys.stdin = open('input.txt', 'r')

N = int(input())
card_list = list(map(int, sys.stdin.readline().split()))
result = {}

for card in card_list:
    cnt = result.get(card)
    if cnt!=None:
        result.update({card: cnt + 1})
    else:
        result.update({card: 1})

M = int(input())
find_list = list(map(int, sys.stdin.readline().strip().split()))

for i in find_list:
    p = result.get(i)
    if p == None:
        print(0, end=' ')
    else:
        print(p, end=' ')
