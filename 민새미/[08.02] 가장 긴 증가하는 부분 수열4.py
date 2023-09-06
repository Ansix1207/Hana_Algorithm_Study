n=int(input())
arr=list(map(int, input().split(" ")))

dp=[1 for _ in range(n)]


for i in range(n):
    for j in range(i):
        if arr[i]>arr[j]:
                dp[i]=max(dp[i], dp[j]+1)

print(max(dp))
# 틀림 -> 왜지..
# d=dict()
# for i in range(n):
#     d[dp[i]]=arr[i]

# dp=list(set(dp))

# for i in dp:
#      print(d[i], end=" ")

answer=[]
k=max(dp)
for i in range(n-1, -1, -1):
    if dp[i]==k:
        answer.append(arr[i])
        k-=1
answer.reverse()
print(*answer)
