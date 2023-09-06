def solution(arr):
    answer = [arr[0]]
    for i in range(len(arr)):
        if arr[i] != answer[-1]:
            answer.append(arr[i])

    return answer


## 효율성 테스트 통과를 못한 코드 -> 70%만 맞음
# pop 코드가 O(1)인데 이것때문에 문제가 걸렸던 건가..
def solution(arr):
    answer = [arr[0]]
    for i in range(len(arr)):
        k = arr.pop(0)
        if k != answer[-1]:
            answer.append(k)
    return answer
