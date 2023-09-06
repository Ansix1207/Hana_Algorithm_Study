n=int(input())

tree=[[] for _ in range(n+1)]

for i in range(n-1):
    a, b= map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

print(tree)