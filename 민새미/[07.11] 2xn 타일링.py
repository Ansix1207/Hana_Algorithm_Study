n=int(input())

k=[0]*(n+2)

k[1]=1
k[2]=2


def tile(i):
    
    if i<3:
        return
    if i>=3:
        tile(i-1)
        k[i]=k[i-2]+k[i-1]
tile(n)
print(k[n]%10007)