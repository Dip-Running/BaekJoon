import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint
arr = [list(map(int, input().split())) for _ in range(4)]

pprint(max(map(max, arr)))