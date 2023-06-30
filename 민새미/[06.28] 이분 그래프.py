## 풀기 어려웠던 문제이다... 그룹을 1과 -1로 구분짓고 이 그룹 자체를 visited배열 내에서 처리하게 한다니...ㅠㅠㅠ
# 코드만 보고 정확하게 파악이 되지 않아 손으로 과정을 그려서 이해했다.. 꼭 다음에 다시 풀어야 하는 문제 같다.

## DFS

import sys

input = sys.stdin.readline

k = int(input())


def dfs(start, group):
    global error

    if error:  # 만약 사이클이 true라면 재귀탈출
        return

    # 해당 그룹으로 등록
    visited[start] = group

    for i in graph[start]:
        if not visited[i]:
            dfs(i, -group)  # 다른 그룹으로 설정
        elif visited[start] == visited[i]:  # 인접한데 같은 그룹이라면
            error = 1  # 에러값 1
            return  # 그후 재귀 리턴


for i in range(k):
    V, E = map(int, input().split())  # v: 정점의 개수, e: 간선의 개수

    graph = [[] for _ in range(V + 1)]  # 빈 그래프 생성
    visited = [0] * (V + 1)
    error = 0

    for j in range(E):
        # 간선의 정보
        u, v = map(int, input().split())  # 인접한 두 정점의 번호 => 즉, 다른 집합에 있는 것
        graph[u].append(v)  # 무방향 그래프
        graph[v].append(u)  # 무방향 그래프

    for i in range(1, V + 1):
        if not visited[i]:
            dfs(i, 1)
            if error:
                break

    if error:
        print("NO")
    else:
        print("YES")

#################################################################################################
## BFS

import sys
from collections import deque

input = sys.stdin.readline


# bfs
def bfs(start, group):
    queue = deque([start])  # 시작 정점 값을 큐에 담는다.
    visited[start] = group  # 시작 정점 그룹을 설정
    while queue:  # 큐가 존재할때까지 돈다.
        x = queue.popleft()  # 큐의 맨앞 원소를 빼낸다.

        for i in graph[x]:  # 해당 정점에서 갈 수 있는 하위 정점들을 돈다.
            if not visited[i]:  # 만약 그 정점들을 아직 방문하지 않았다면
                queue.append(i)  # 그 정점들을 추가하고
                visited[i] = -1 * visited[x]  # 상위 정점과 다른 그룹으로 편성
            elif visited[i] == visited[x]:  # 만약 정점들을 이미 방문했었는데 같은 그룹이라면
                return False  # False를 바로 리턴
    return True  # 위의 조건에 걸리지 않았다면 True를 리턴


for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for i in range(V + 1)]  # 빈 그래프 생성
    visited = [False] * (V + 1)  # 방문한 정점 체크

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)  # 무방향 그래프
        graph[b].append(a)  # 무방향 그래프

    for i in range(1, V + 1):
        if not visited[i]:  # 방문한 정점이 아니면, bfs 수행
            result = bfs(i, 1)
            if not result:
                break

    print("YES" if result else "NO")



######################################################
# 혼자 대충 풀어본 코드..ㅎ 틀린 코드임

# import sys

# input = sys.stdin.readline

# k = int(input())


# for i in range(k):
#     V, E = map(int, input().split())  # v: 정점의 개수, e: 간선의 개수

#     one = list()
#     two = list()

#     visited = [0] * (V + 1)

#     k = 0
#     for j in range(E):
#         # 간선의 정보
#         u, v = map(int, input().split())  # 인접한 두 정점의 번호 => 즉, 다른 집합에 있는 것

#         if not visited[u] or u not in two:  # 방문하지 않은 정점이면서, 어느 하나의 집합에 속하지 않았으면
#             visited[u] = 1
#             visited[v] = 1
#             k += 1
#             one.append(u)
#             two.append(v)
#         else:
#             print("NO")
#             break

#     if k == E:
#         print("YES")
