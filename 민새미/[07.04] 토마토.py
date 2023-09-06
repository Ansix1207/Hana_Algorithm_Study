from collections import deque

n, m=map(int, input().split())

maps=list()
# for i in range(m):
    # k=list(map(int,input().split()))
    # maps.append(k)

maps=[list(map(int, input().split())) for _ in range(m)]


# print(maps)

dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]
q=deque()
res=0

for i in range(m):
    for j in range(n):
        if maps[i][j]==1:
            q.append((i, j))


def bfs():
    while(q):
        x, y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # if 0<=nx<n and 0<=ny<m and maps[nx][ny]==0:
            #     maps[nx][ny]=maps[nx][ny]+1
            #     q.append((nx, ny))
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if maps[nx][ny]==0:
                maps[nx][ny]=maps[x][y]+1
                q.append((nx, ny))


bfs()
# print(maps)
for i in range(m):
    for j in range(n):
        if maps[i][j]==0:
            print(-1)
            exit(0)
    res=max(res, max(maps[i]))
print(res-1)