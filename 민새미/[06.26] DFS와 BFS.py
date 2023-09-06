#1260_DFS와 BFS

# 풀이) 단순하게 푸는 문제이면서, DFS와 BFS가 동시에 진행되기 때문에 방문처리를 신경써서 해줘야한다!
# 각 경로는 matrix 배열에 1로 담고,
# DFS를 할 때는 visited 배열을 0으로 초기화 한 상태에서 방문을 안했을 때는 0일때로 한다면,
# BFS를 할 때는 DFS로 방문하여 1로 되어 있던 값들로 존재하기 때문에 1이 방문을 하지 않은 것으로 가정이 되어, 방문 안했을 때가 1이 된다.
# 옛날에 풀었어서 코드 다시 복습하자는 느낌으로 학습했는데.. 확실히 시간이 지나니까 잊은 것 같긴 하다..!

n, m, v = map(int, input().split())

matrix = [[0] * (n + 1) for i in range(n + 1)]

visited = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1


def dfs(v):
    visited[v] = 1

    print(v, end=" ")

    for i in range(1, n + 1):
        # 방문 안했고, 인접한 곳이라면
        if visited[i] == 0 and matrix[v][i] == 1:
            dfs(i)


def bfs(v):
    q = [v]

    # dfs를 완료한 visited 배열 (1로 되어있음)에서 방문 체크
    visited[v] = 0

    while q:
        v = q.pop(0)
        print(v, end=" ")
        for i in range(1, n + 1):
            if visited[i] == 1 and matrix[v][i] == 1:
                q.append(i)
                visited[i] = 0


dfs(v)
print()
bfs(v)
