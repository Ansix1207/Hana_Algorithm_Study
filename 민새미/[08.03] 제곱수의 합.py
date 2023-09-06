
n=int(input())


# 처음코드
# 100000의 제곱부터 1씩 내려가서 해서 n의 값보다 작아지면 그 값을 가장 큰 제곱값이라 두고 1 빼면서 이전에 제곱했던 값에서 더하면서 아래 제곱을 찾아감
# arr=[i for i in range(n+1)]
# res=[i*i for i in range(n+1)]

# print(arr)
# print(res)

# r=list()
# for i in range(1,n+1):
#     if res[i]<=n:
#         r.append(res[i])

# 무조건 큰 수의 제곱수들로만 나타내는 것이 정답이 아닌것을 알게됨 -> ex)18 => 2
# def c(k, cnt):
#     for i in range(len(r)-1, -1, -1):
#         if k+r[i]<=n:
#             k=k+r[i]
#             cnt+=1
#             if k==n:
#                 print(cnt)
#                 exit(0)
#             c(k, cnt)

# c(0, 0)


dp=[i for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i):
        if (j*j)>i:
            break
        if dp[i]>dp[i-j*j] +1:
            dp[i]=dp[i-j*j] +1
print(dp[n])

