# 참고한 풀이1 =>  idx=location 이거로 프로세스의 위치를 추적함
from collections import deque


def solution(priorities, location):
    answer = 1
    q = deque(priorities)
    idx = location  # 이거로 프로세스의 위치를 추적함.. idx 값을 변경해서 추적하는 방법은 생각도 못했음..
    while len(q) > 1:
        tmp = q.popleft()
        if tmp < max(q):
            q.append(tmp)
            if idx == 0:
                idx = len(q) - 1
            else:
                idx -= 1
        else:
            if idx == 0:
                return answer
            else:
                answer += 1
                idx -= 1

    return answer


# 참고한 풀이2 =>튜플, any 함수 사용함.
def solution(priorities, location):
    answer = 0
    # 튜플로 처음 순서를 기억한다
    queue = [(i, p) for i, p in enumerate(priorities)]
    while 1:
        cur = queue.pop(0)
        # any로 조건을 체크
        if any(cur[1] < q[1] for q in queue):  # 튜플이니까 인덱스 [1]로 가져옴.
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
    return answer


# 내가 처음 풀었던 풀이.. 로직은 짰지만, 그 순서를 기억하게 하는게 좀 어려웠음 ㅠㅠㅠㅠㅠ
# 단순 스택으로 푸는건 아닐거 같고, 큐를 이용하는 것 같아보였음 왜냐면 계속 돌아가야하니까!
# 딕셔너리로 {'A': 2, 'B': 1, 'C': 3, 'D': 2} 로라도 저장해서 하려고 했는데 딕셔너리는 value값으로 key값을 가져오려면 key값이 겹치면 안되는데 겹쳐서 문제가 발생해버림..
# 결국 풀이를 보고 해결함.
def solution(priorities, location):
    answer = 0
    k = 0
    a = len(priorities)
    res = list()
    i = 0
    p = priorities.copy()

    al = list()
    kk = ord("A")
    for i in range(a):
        al.append(chr(kk))
        kk += 1

    d = dict(zip(al, priorities))
    print(d)
    dd = list()

    while 1:
        if len(res) == len(priorities):
            break
        if p[i % a] == max(p):
            res.append(p.pop(i % a))

            k += 1
            a -= 1
            print(res)

        else:
            i += 1

    return answer
