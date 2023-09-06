def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a = commands[i][0]
        b = commands[i][1]
        c = commands[i][2]
        arr = sorted(array[a - 1 : b])
        answer.append(arr[c - 1])
    return answer
