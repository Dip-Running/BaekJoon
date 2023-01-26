N, M = map(int, input().split())

Heard = set()
See = set()

for i in range(N):
    Heard.add(input())

for j in range(M):
    See.add(input())

HS = list(Heard & See)
HS.sort()
print(len(HS))
for i in HS:
    print(i)