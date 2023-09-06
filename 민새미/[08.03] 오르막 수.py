# 이 문제도 이해가 안갔음.. 그래서 참고해서 풀었음.. 좀 문제만 정확히 이해했으면 풀 수 있지 않았을까라는 생각

n=int(input())

dp=[1]*10
for i in range(1, n):
    for j in range(1, 10):
        dp[j]+=dp[j-1]
print(sum(dp) %10007)