from collections import deque
n, k = map(int, input().split())

MAX=10**5
visited=[0]*(MAX+1) 

def bfs():
    q=deque()
    q.append(n)
    while q:
        x=q.popleft()
        if x==k:
            print(visited[x])
            break
        for i in (x-1, x+1, 2*x):
            if 0<=i<=MAX and not visited[i]: 
                q.append(i)
                # print(i)
                visited[i]=visited[x]+1
    return

bfs()