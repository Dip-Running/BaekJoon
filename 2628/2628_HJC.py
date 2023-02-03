import sys
sys.stdin = open('input.txt', 'r')

y, x = map(int, input().split())
n = int(input())
cutx, cuty = [x], [y]
for i in range(n):
    cutxy, cutpos = map(int, input().split())
    if cutxy == 1:
        cuty.append(cutpos)
    else:
        cutx.append(cutpos)
cutx.sort()
cuty.sort()
# print(cutx, cuty)
betx, bety = [cutx[0]], [cuty[0]]

for i in range(len(cutx)-1):
    betx.append(cutx[i+1] - cutx[i])
betx.append(x-cutx[-1])
for i in range(len(cuty)-1):
    bety.append(cuty[i+1] - cuty[i])
bety.append(y-cuty[-1])
# print(betx, bety)
print(max(betx) * max(bety))