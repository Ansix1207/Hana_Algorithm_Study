from collections import deque

dx=[1, 2, 1, 2, -1, -2, -1, -2]
dy=[2, 1, -2, -1, 2, 1, -2, -1]

def bfs(a, b):
    q=deque()
    q.append((a, b))
    while(q):
        x, y= q.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=k or ny<0 or ny>=k:
                continue
            if maps[nx][ny]==0:
                maps[nx][ny]=maps[x][y]+1
                # print(maps)
                q.append((nx, ny))
    return maps[movex][movey]-1


tc = int(input())

for i in range(tc):
    k=int(input())
    maps=[[0]*k for _ in range(k)]
    

    currentx, currenty=map(int, input().split())
    maps[currentx][currenty]=1
    movex, movey = map(int, input().split())
    print(bfs(currentx, currenty))
