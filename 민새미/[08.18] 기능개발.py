def solution(progresses, speeds):
    answer = []
    arr = []
    for i in range(len(progresses)):
        k = 100 - progresses[i]
        if k % speeds[i] == 0:
            arr.append(int(k / speeds[i]))
        else:
            arr.append(int(k / speeds[i]) + 1)

    a = arr[0]
    cnt = 1
    for i in range(1, len(arr)):
        if a >= arr[i]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            a = arr[i]  # 이 부분이 빠져서 틀렸었음..!!!
    answer.append(cnt)

    return answer
