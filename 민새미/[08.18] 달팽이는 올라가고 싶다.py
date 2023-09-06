# 이 계산식으로 떠올리는게 생각보다 어려움 ㅠ 수학 문제라고 생각하고 여러 점화식을 도출했는데도 다 틀려서 결국 참고함

a, b, v = map(int, input().split())

if a > v:
    print(1)
else:
    if (v - a) % (a - b) == 0:
        print((v - a) // (a - b) + 1)
    else:
        print((v - a) // (a - b) + 2)
