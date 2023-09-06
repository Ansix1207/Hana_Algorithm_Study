# 혼자 다 품!!
# 힙은 작은 값을 무조건 pop하기 때문에 h1이라는 배열을 하나 더 만들어서 -로 바꿔서 가장 큰 값을 가장 작은값으로 변환해서 가장 큰 값이 나가도록 함.
import heapq


def solution(operations):
    answer = []
    h = []
    h1 = []
    k = 0
    for i in range(len(operations)):
        a, b = operations[i].split()
        if a == "I":
            if len(h) < k:
                k -= 1
            heapq.heappush(h, int(b))
            k += 1

        elif a == "D":
            if len(h) == 0:
                continue
            if b == "1":
                for i in range(len(h)):
                    heapq.heappush(h1, -h[i])
                heapq.heappop(h1)
                h = []
                for j in range(len(h1)):
                    heapq.heappush(h, -h1[j])
                h1 = []
            elif b == "-1":
                heapq.heappop(h)
    if len(h) != 0:
        answer.append(max(h))
        answer.append(min(h))
    if len(h) == 0:
        answer = [0, 0]

    return answer
