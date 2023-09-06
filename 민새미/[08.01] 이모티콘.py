# s=int(input())

# display=1 #화면에 보여지는 이모티콘 수
# cnt=0 #총 연산 시간
# clip= 0 #클립보드에 있는 이모티콘 수

# clip=display

# display=clip

# display-=1

# def check(n):
#     if n==1:
#         clip=display
#     elif n==2:
#         display=clip
#     elif n==3:
#         display-=1


# def dfs(n):
#     if display==s:
#         return cnt
#     for i in range(3):
#         check(i) #음... 모르겠네..

# 거의 다 풀었던 거 같은데ㅠㅠㅠㅠ DFS로 풀까 했었는데 담에 풀때는 풀 수 있었으면 좋겠다..!
from collections import deque
s=int(input())

q=deque()
q.append([1, 0, 0])
visited=[[0]*1001 for _ in range(1001)]
visited[1][0]=1

while q:
    screen, clip, cnt = q.popleft()

    if screen ==s:
        print(cnt)
        break

    for i in range(3):
        if i ==0:
            new_clip, new_screen = screen, screen
        elif i==1:
            new_clip, new_screen = clip, screen+clip
        else:
            new_clip, new_screen = clip, screen-1

        if new_screen >=1001 or new_screen <0 or new_clip >=1001 or new_clip<0 or visited[new_screen][new_clip]:
            continue

        visited[new_screen][new_clip] = 1
        q.append([new_screen, new_clip, cnt+1])
