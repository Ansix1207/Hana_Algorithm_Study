n=int(input())
arr=list()
for i in range(n):
    k=list(map(int, input().split()))
    arr.append(k)

for i in range(1,n): # 1부터 시작하는 이유는 다음 입력값이 이전 입력값의 최소값을 사용하기때문이다
    arr[i][0]=min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1]=min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    arr[i][2]=min(arr[i-1][0], arr[i-1][1]) + arr[i][2]

print(min(arr[n-1][0],arr[n-1][1],arr[n-1][2]))
