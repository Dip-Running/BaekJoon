import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    Anum, *Acard = map(int, input().split())
    Bnum, *Bcard = map(int, input().split())
    Acard = list(Acard)
    aarr = [0]*5
    barr = [0]*5
    for i in range(len(Acard)):
        aarr[Acard.pop()] += 1
    for i in range(len(Bcard)):
        barr[Bcard.pop()] += 1
    for i in range(4, 0, -1):
        if aarr[i] > barr[i]:
            print('A')
            break
        elif aarr[i] < barr[i]:
            print('B')
            break
        elif aarr[i] == barr[i]:
            continue
    else:print('D')