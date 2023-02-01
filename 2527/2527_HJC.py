# import sys
# sys.stdin = open("input.txt", "r")

## 2차원 배열 입력
arr = [list(map(int, input().split())) for _ in range(4)]

for i in arr:
    # 여기서 i[인덱스]로 비교하면 무슨짓을 해도 틀렸습니다 라고 뜸
    # 아마도 참조로 값을 확인해서 그런가 싶음
    # 변수 선언하고 새로 넣으니 돌아가길래...어이는 없지만...
    x1, y1, p1, q1, x2, y2, p2, q2 = i
    # case (d)
    # 사각형 1의 낮은거보다 2의 큰게 더 작거나
    # 사각형 1의 큰게 2의 작은거보다 작으면 만나지 않으므로 d 출력
    if p1 < x2 or p2 < x1 or y1 > q2 or q1 < y2:
        print('d')

    # 사각형 1의 낮은거랑 사각형 2의 큰게 같거나 사각형2의 작은거랑 사각형 1의 큰거 비교
    elif x1 == p2 or x2 == p1:
        # case (c)
        # 같은데 y좌표도 같은 위치다? 그럼 접점이 있는거니까 c출력
        if q1 == y2 or q2 == y1:
            print('c')
        # case (b)
        # 아니면 선이 겹치므로 b 출력
        else:
            print('b')
    elif q1 == y2 or q2 == y1:
        print('b')
    # case (a)
    # 다 아니면 a 출력
    else:
        print('a')