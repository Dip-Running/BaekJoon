def position():
    w, h = map(int, input().split())
    x, y = map(int, input().split())
    n = int(input())

    x = [(x + n) % w if (x + n)//w % 2 == 0 else w - (x + n) % w] # (x+n)//w %2 == 0 : 오른쪽  1이면 왼쪽 
    y = [(y + n) % h if (y + n)//h % 2 == 0 else h - (y + n) % h] # (y + n)//h % 2 == 0 : 위쪽 1이면 아래쪽
    return x+y
result = position()
print(*result)