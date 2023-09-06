from collections import deque
n, m =map(int, input().split())

maps=list()
for i in range(n):
    k=list(map(int, input()))
    maps.append(k)

# print(maps)


dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

def bfs(a, b):
    q=deque()
    q.append((a, b))
    maps[a][b]=0
    res=0
    while(q):
        x, y=q.popleft()
        

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if maps[nx][ny]!=1:
                continue
            if maps[nx][ny]==1:
                
                maps[nx][ny]+=maps[x][y]
                
                q.append((nx, ny))

            if nx==n-1 and ny==m-1:
                res= maps[n-1][m-1]

    return res+1
                

print(bfs(0, 0))