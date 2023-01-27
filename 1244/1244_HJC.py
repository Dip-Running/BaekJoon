#import sys
#sys.stdin = open("input.txt", "r")
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, -1)
m = int(input())

def switch(index):
    if arr[index] == 0:
        arr[index] = 1
    else:
        arr[index] = 0

for _ in range(m):
    x, y = map(int, input().split())
    if x == 1:
        for i in range(y, n+1, y):
            switch(i)
    if x == 2:
        switch(y)
        for i in range(n // 2):
            if y-i < 1 or y+i > n or arr[y-i] != arr[y+i]:
                break
            else:
                switch(y-i)
                switch(y+i)

for i in range(1, n+1):
    print(arr[i], end = ' ')
    if i % 20 == 0 :
        print()
