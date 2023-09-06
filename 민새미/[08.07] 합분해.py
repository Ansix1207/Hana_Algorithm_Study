# 좀 더 규칙 찾아보고자 해볼걸.. 너무 빠르게 포기하긴 했음..ㅠ

n, k = map(int, input().split())

dp = [[0] * 201 for i in range(201)]

for i in range(201):
    dp[1][i] = 1
    dp[2][i] = i + 1


for i in range(2, 201):
    dp[i][1] = i
    for j in range(2, 201):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000000

print(dp[k][n])
