import sys
sys.stdin = open('input.txt', 'r')
#--ps) 감사합니다 진욱님--#
import sys
input = sys.stdin.readline
w, h = map(int, input().split())    # size
x, y = map(int, input().split())    # pos
n = int(input())    # time

nx = (x + n) % w if ((x + n) // w) % 2 == 0 else w - ((x + n) % w)
ny = (y + n) % h if ((y + n) // h) % 2 == 0 else h - ((y + n) % h)
print(nx, ny)