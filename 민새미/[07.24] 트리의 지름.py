## 트리 만들고 각 트리의 깊이 구해서 최댓값 2개 나오면 더해서 반환하기

import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**5)

n=int(input())
tree =[[] for _ in range(n+1)]
# 양방향 연결 리스트로 저장
# 루트 노드 1인 부모 -자식 트리라 하더라도
# 루트의 지름을 구하려면 임의의 노드에서 부모-자식 상하 관계에 구애받지 않고 모든 노드를 순회할 수 있어야하기 때문
for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))

# print(tree)

def dfs(node, cost):
    for n, w in tree[node]:
        res=cost+w
        if visited[n] ==-1:
            visited[n]=res
            dfs(n, res)
    return

# 첫번째 DFS로 지름의 양 끝점 중 하나 구하기
visited=[-1]*(n+1)
visited[1]=0

dfs(1, 0)
idx, tmp=0, 0
for i in range(1, len(visited)):
    if visited[i]>tmp:
        tmp=visited[i]
        idx=i

# 두번째 DFS로 나머지 트리의 지름 끝점 하나를 찾고 지름 구하기
visited=[-1]*(n+1)
visited[idx]=0
dfs(idx, 0)

print(max(visited))