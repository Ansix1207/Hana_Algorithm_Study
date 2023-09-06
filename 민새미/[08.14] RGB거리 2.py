n=int(input())

arr=[list(map(int, input().split()))for _ in range(n)]

ans=E=1e9
for i in range(3):
    dp=[[E, E, E] for _ in range(n)] # dp가 각 R, G, B로 시작했을 때
    dp[0][i]=arr[0][i] #처음 집 색칠
    for j in range(1, n): #2번째 집부터 R, G, B로 색칠했을 때 최소값 갱신
        dp[j][0]=arr[j][0]+min(dp[j-1][1], dp[j-1][2])
        dp[j][1]=arr[j][1]+min(dp[j-1][0], dp[j-1][2])
        dp[j][2]=arr[j][2]+min(dp[j-1][0], dp[j-1][1])
    for k in range(3):
        if i !=k: #첫번째 집과 N번째 집이 다른 경우만 선택
            ans=min(ans, dp[-1][k])

print(ans)