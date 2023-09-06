# 결국 참고해서 풀었다ㅜㅠ 아래 코드를 보면 여러 방법을 시도한 코드를 볼 수 있다.. 틀리긴 했지만

# 설명
# 3을 곱하는 이유는 2번째 예시를 풀 때 이유를 알게 된다.
# 계산할 때 사전값으로만 정렬을 한다면 [9,5,34,30,3] 이렇게 정렬된다.
# 하지만 3이 30보다 앞에 와야한다.
# number는 1000이하의 숫자이므로 최대값을 생각해 3을 곱해줬고,
# 3을 곱하게 되면 [999, 555, 343434, 303030, 333] 이렇게 될 것이고, 정렬을 하게 되면 [999, 555, 343434, 333, 303030]이 된다.


def solution(numbers):
    answer = ""
    n_str = [str(num) for num in numbers]  # 1. 사전 값으로 정렬하기
    # 2. number는 1000이하의 숫자이므로 x3(반복)한 값으로 비교. (문자를 *3 하니까 3이라면 333이 됨)
    n_str.sort(key=lambda num: num * 3, reverse=1)

    return str(int("".join(n_str)))


# 처음 테스트 코드는 통과한 코드
# 근데 시간 초과로 다 틀리게 됨..! 안될 것 같았지만ㅎ
from itertools import permutations


def solution(numbers):
    answer = ""
    k = ""
    res = []
    result = []
    arr = list(permutations(numbers))
    for i in arr:
        for j in range(len(i)):
            k += str(i[j])
        res.append(k)
        k = ""
    for i in range(len(res)):
        result.append(int(res[i]))
    answer = str(max(result))
    return answer


# 혼자 이것저것 풀어보려고 했을떄는 숫자의 첫번쨰 자릿수 비교해서 max로 꺼내고 리스트에서는 삭제하고 뭐 그런식으로 진행하려고 했는데
# max()로 찾게 되면 숫자가 33, 34 이렇게 되면 3 다음의 자릿수를 비교해야하는데 너무 번거롭다..ㅠ


def solution(numbers):
    answer = ""
    res = []
    while 1:
        if len(numbers) == 0:
            break
        else:
            res = []
            for i in range(len(numbers)):
                res.append(int(str(numbers[i])[0]))
            k = max(res)
            p = res.index(k)
            answer += str(numbers[p])
            numbers.pop(p)

    return answer
