# 바꿔서 정렬하는것 까진 생각을 했는데 구현까지 나 스스로 하는게 좀 힘들었고, 코드를 쓰는 것 그니까 구현 능력이 좀 부족한 것 같음 ㅠㅠ

import heapq


def solution(jobs):
    answer = 0
    now, i, start = 0, 0, -1
    h = []
    while 1:
        if i >= len(jobs):
            break

        for j in jobs:
            if start < j[0] <= now:  # 시작시점 지나고부터 지금까지 작업 가능한 그 사이 시간 확인
                heapq.heappush(h, [j[1], j[0]])  # 반대로 넣어서 정렬함!

        if len(h) > 0:
            cur = heapq.heappop(h)
            start = now  # if문 때문에 처리해줘야함. #지금까지 작업한 것 기준으로 시작
            now += cur[0]
            answer += now - cur[1]  # 순수하게 이동한 거리를 구해야하기 때문에 now에서 cur[1]을 빼줌
            i += 1
        else:
            now += 1  # 지금 시점에서 할 수 있는 작업이 없을때 1씩 증가시킴.
    return int(answer / len(jobs))
