import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000001)


n = int(input())
arr = [0] * (1000001)
arr[1] = 1
arr[2] = 2
arr[3] = 4
# 아예 미리 만들어놓고 해야지 됨... 원래는 입력받자마자 for문을 돌렸는데 시간초과가 됐음
# for i in range(4, k+1):
#     arr[i] = (arr[i - 3] + arr[i - 2] + arr[i - 1]) % 1000000009
for i in range(4, 1000001):
    arr[i] = (arr[i - 3] + arr[i - 2] + arr[i - 1]) % 1000000009


for i in range(n):
    k = int(input())
    print(arr[k])
