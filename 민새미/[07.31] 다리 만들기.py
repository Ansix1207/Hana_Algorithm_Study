from collections import deque

n=int(input())

maps=list()
for i in range(n):
    maps.append(list(map(int, input().split())))

visited=[[0] * n for _ in range(n)]

dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]

k=1
def bfs(a, b):
    q=deque()
    q.append((a, b))
    visited[a][b]=1
    while(q):
        x, y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if maps[nx][ny]==0:
                continue
            if maps[nx][ny]==1 and visited[nx][ny]==0:
                maps[nx][ny]=k
                q.append((nx, ny))
                visited[nx][ny]=1
                


for i in range(n):
    for j in range(n):
        if maps[i][j]==1 and visited[i][j]==0:
            visited[i][j]=1
            maps[i][j]=k
            bfs(i, j)
            k+=1


res=int(1e9)

#최단 거리 구하기 (이 부분을 생각하기 좀 어려웠달까)

def bfs2(v):
    q2=deque()
    dist=[[-1]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maps[i][j]==v:
                dist[i][j]=0
                q2.append((i, j))
    
    while q2:
        x, y=q2.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                #다른 섬 만났다=> 연결됨
                if maps[nx][ny] and maps[nx][ny] !=v:
                    return dist[x][y]
                #물이고 아직 다리 없는 곳
                elif maps[nx][ny]==0 and dist[nx][ny]==-1:
                    dist[nx][ny]=dist[x][y]+1
                    q2.append((nx, ny))

    return int(1e9)

# 최단 거리 구하기
for i in range(1, k):
    # print(bfs2(i))
    res=min(res, bfs2(i))
print(res)