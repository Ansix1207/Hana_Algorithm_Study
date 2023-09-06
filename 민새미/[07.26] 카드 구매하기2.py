n=int(input())
cards=[0]
cards+=list(map(int, input().split()))

def dp(n):
    arr=[0]*(n+1)
    

    for i in range(1,n+1):
        save=list()
        for j in range(1,i+1):
            save.append(cards[i])
            save.append(arr[i-j]+cards[j])
            arr[i]=min(save)
        
    # print(arr)
    return arr[n]

print(dp(n))