import bisect

n=int(input())

arr=list(map(int, input().split()))

dp=[1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i]=max(dp[i], dp[j]+1)

print(max(dp))

# 이진탐색으로 푸는 방법
# dp=[arr[0]]

# for i in range(n):
#     if arr[i]>dp[-1]:
#         dp.append(arr[i])
#     else:
#         idx=bisect.bisect_left(dp, arr[i]) #dp가 정렬되어있다는 가정하에 arr[i]값이 들어갈 위치 반환
#         dp[idx]=arr[i]

# print(len(dp))