from collections import deque

dx=[1, -1, 0, 0, -1, 1, -1, 1]
dy=[0, 0, 1, -1, -1, -1, 1, 1]


def bfs(a, b):
    q=deque()
    q.append((a, b))
    maps[a][b]=0
    while(q):
        x,y=q.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=h or ny<0 or ny>=w:
                continue
            if maps[nx][ny]==0:
                continue
            if maps[nx][ny]==1:
                q.append((nx, ny))
                maps[nx][ny]=0
    return 1




while(1):
    w, h=map(int, input().split())

    if (w==0 and h==0):
        break

    maps=list()
    for i in range(h):
        a=list(map(int, input().split()))
        maps.append(a)
    count=0
    for i in range(h):
        for j in range(w):
            if maps[i][j]==1:
                count+=bfs(i, j)

    print(count)



