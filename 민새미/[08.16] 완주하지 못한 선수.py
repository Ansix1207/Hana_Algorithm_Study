from collections import Counter


# Counter({'h': 0, 'e': 1, 'l': 4, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
def solution(participant, completion):
    answer = ""
    k = Counter(participant) - Counter(completion)
    for i in k.keys():
        answer = i
    return answer
