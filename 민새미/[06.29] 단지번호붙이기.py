from collections import deque
import sys

inpu=sys.stdin.readline

n=int(input())

maps=list()
for i in range(n):
    k=list(map(int, input()))
    maps.append(k)

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

def bfs(a, b):
    k=1
    q=deque()
    q.append((a, b))
    maps[a][b]=0

    while(q):
        x, y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if maps[nx][ny]==0:
                continue
            if maps[nx][ny]==1:
                q.append((nx, ny))
                maps[nx][ny]=0
                k+=1
    return k


res=0
result=list()
for i in range(n):
    for j in range(n):
        if maps[i][j]==1:
            ans=bfs(i, j)
            result.append(ans)
            res+=1

result.sort()
print(res)
for i in range(res):
    print(result[i])
