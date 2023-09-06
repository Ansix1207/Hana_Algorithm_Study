#1182_부분수열의 합

# 조합 문제이다. 처음에는 백트래킹 방식으로 풀어보았다. 조합으로 각 원소를 모두 더해준다는 말에 혼자 2개 이상의 조합이겠다고 생각이 들어서 계속 틀렸었다..ㅠ
# 그리고 dfs로 들어갈 때마다 start 값이 i+1씩 가야하는데 start+1이라고 써서 오류가 나기도 했다.
# 잠을 못자서 그런지 머리를 쓰다가 말았달까...?
# 아무튼 DFS로 접근도 어느정도 했고, 조합 관련된 코드는 참고하되 직접 어디가 문제인지 생각하면서 풀었다.

# DFS 로 푼 코드

import sys
input = sys.stdin.readline


n, s = map(int, input().split())

arr = list(map(int, input().split()))

visited = [0] * n
cnt = 0
# 경우의 수를 다 구해야 함.. (조합으로)
out = list()


def dfs(depth, m, start):
    global cnt

    k = 0
    if depth == m:
        # print(out)
        for i in range(m):
            k += out[i]
        if k == s:
            # print(out)

            cnt += 1
            return
    for i in range(start, n):
        if not visited[i]:
            out.append(arr[i])
            visited[i] = 1
            dfs(depth + 1, m, i + 1)
            visited[i] = 0
            out.pop()


for i in range(1, n+1):
    dfs(0, i, 0)


print(cnt)


## 다른 코드 방식도 있을까 찾던 중 조합 라이브러리를 이용한 코드가 있었다.
## 라이브러리로도 문제가 당연히 풀리겠지만 느리지 않을까 생각을 해서 그냥 그렇게 안풀었는데.. 
## 돌려보니 훨씬 더 빨랐다!! (시간 차이가 무려 DFS- 6892 ms / combinations - 368 ms) 약 20배 차이..??????!?
## DFS코드 짜는게 더 어려운데 왜 라이브러리가 더 빠른걸까..ㅎㅠㅠㅠ 괜히 보람이 없달까

## 아래는 라이브러리로 해결한 코드이다.

import sys
from itertools import combinations

input = sys.stdin.readline


n, s = map(int, input().split())

arr = list(map(int, input().split()))
cnt = 0
for i in range(1, n + 1):
    comb = combinations(arr, i)

    for k in comb:
        if sum(k) == s:
            cnt+=1

print(cnt)


###############################################################################################################################

# 14391_종이조각.py

# 일단 문제부터 이해가 잘 안된달까..? 근데 어떻게 해결할지도 가늠도 안오고..
#  그래서 문제 이해 할겸, 코드 분석 할겸 찾아보았다..
#  비트 연산자를 이용하여 해결하는 문제였다

 #코드는 아래와 같은데 ... 이해가 잘 안된다 스터디 사람들과 함께 풀어보면 좋은 문제라고 생각이 든다..ㅠㅠㅠ

def bitmask():
    global maxAns
    # 비트마스크로 2^(N*M)의 경우의 수를 따져본다 - 한칸당 가로 또는 세로로 갈 수 있는 경우의 수
    for i in range(1 << n * m):
        total = 0
        # 가로 합 계산
        for row in range(n):
            rowsum = 0
            for col in range(m):
                # idx 는 이차원 배열을 일렬로 늘렸을때의 인덱스가 어디인지 의미
                idx = row * m + col
                # 가로일때
                if i & (1 << idx) != 0:
                    rowsum = rowsum * 10 + arr[row][col]
                # 세로일때 앞에서 나온 수를 total에 더하고 rowsum 초기화
                else:
                    total += rowsum
                    rowsum = 0
            total += rowsum

        # 세로 합 계산
        for col in range(m):
            colsum = 0
            for row in range(n):
                # idx 는 이차원 배열을 일렬로 늘렸을때의 인덱스가 어디인지 의미
                idx = row * m + col
                # 세로일때
                if i & (1 << idx) == 0:
                    colsum = colsum * 10 + arr[row][col]
                # 가로일때 앞에서 나온 수를 total에 더하고 colsum 초기화
                else:
                    total += colsum
                    colsum = 0
            total += colsum
        maxAns = max(maxAns, total)


n, m = map(int, input().split())

arr = [list(map(int, input())) for _ in range(n)]

maxAns = 0
bitmask()
print(maxAns)



