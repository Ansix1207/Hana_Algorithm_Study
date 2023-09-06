import sys
input=sys.stdin.readline

def cycle(color, x, y, cnt, start_x, start_y):
    global ans
    # 이미 사이클을 찾았다면 종료
    if ans is True:
        return
    #4가지 방향에 대하여
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        
        #사이클이 존재(4개 이상 점 연결, 처음 시작지점 도달)한다면
        if cnt >=4 and nx == start_x and ny==start_y:
            #정답 존재 표시
            ans=True
            return
        #색깔이 같고 아직 방문하지 않았다면
        if board[nx][ny]==color and visited[nx][ny]==0:
            visited[nx][ny]=1
            cycle(color, nx, ny, cnt+1, start_x, start_y)
            visited[nx][ny]=0

#게임 시작 함수
def game_start():
    # 이중 for문 하는 이유는 그래프의 다양한 색상이 있기 때문!
    for i in range(n):
        for j in range(m):
            start_x =i
            start_y= j
            visited[start_x][start_y]=1
            #해당 색상을 선택해서 사이클을 검사했는데 안나오면 다음 칸으로 이동해서 거기선 사이클 없는지 탐색!
            cycle(board[i][j], i , j, 1, start_x, start_y)
            # 이미 사이클이 존재한다면 굳이 사이클이 있는지 탐색하지 않아도 됨(시간 단축!)
            if ans:
                return 'Yes'
    return 'No'




n, m = map(int, input().split())
# board=[[a for a in input().rstrip()] for _ in range(n)]

board=list()
for _ in range(n):
    k=list(input().rstrip())
    board.append(k)

print(board)

visited=[[0] * m for _ in range(n)]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

ans = False
print(game_start())