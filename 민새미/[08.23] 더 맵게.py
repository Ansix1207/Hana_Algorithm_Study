# 힙을 어떻게 써야할지 몰라서 참고해서 품
# 코드 자체 해석해서 푸는것은 어렵지 않았지만 파이썬으로 힙을 어떻게 쓸지 알아야했음
# 근데 여기서 중요한건 try except를 안쓰면 틀린다는 것  왜냐하면, 모든 음식의 스코빌 지수를 K이상으로 만들수 없는 경우에는 -1을 리턴함!
import heapq


def solution(scoville, K):
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)

    mix_cnt = 0
    while 1:
        if heap[0] >= K:
            break
        try:  # try except으로 처리함 (처음 봄!)
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        mix_cnt += 1
    return mix_cnt


# 방식 2 ( 이 코드가 내가 쓸법한 코드!)
import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        mix = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return answer


# 맞을거라고 생각도 안했지만 일단 끄적이고 테케만 맞았음 당연히 틀림ㅎㅎㅎ
def solution(scoville, K):
    answer = 0
    scoville = sorted(scoville)

    res = 0
    cnt = 0
    while 1:
        a = scoville.pop(0)
        b = scoville.pop(0)
        cnt += 1
        res = a + (2 * b)
        if res >= K:
            answer = cnt
            break

        scoville.append(res)
        scoville = sorted(scoville)

    return answer
