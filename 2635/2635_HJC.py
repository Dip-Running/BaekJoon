import sys
sys.stdin = open('input.txt', 'r')

num = int(input())
Max_lst = []
Max_cnt = len(Max_lst)
for i in range(1, num + 1):
    num_lst = [num]
    num_lst.append(i)
    j = 1
    while num_lst[j-1] - num_lst[j] >= 0:
        num_lst.append(num_lst[j-1] - num_lst[j])
        j += 1
        # print(num_lst)
    if Max_cnt < len(num_lst):
        Max_lst = num_lst
    Max_cnt = len(Max_lst)

print(Max_cnt)
print(*Max_lst)