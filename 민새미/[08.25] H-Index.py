def solution(citations):
    answer = 0
    k = len(citations)
    c = sorted(citations)
    for i in range(k):
        if c[i] >= k - i:
            return k - i
    return 0
