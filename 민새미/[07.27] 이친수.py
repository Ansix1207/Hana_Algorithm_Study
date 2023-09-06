n=int(input())
arr=[0]*(n+2)
arr[1]=1
arr[2]=1
def dp(n):
    
    if n<3:
        return(arr[n])
    for i in range(3, n+1):
        arr[i]=arr[i-1]+arr[i-2]
    return arr[n]

print(dp(n))
