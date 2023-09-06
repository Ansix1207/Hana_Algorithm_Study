def solution(s):
    answer = True
    res = list()
    for i in range(len(s)):
        if s[i] == "(":
            res.append("(")
        elif s[i] == ")":
            if len(res) == 0:
                return False
            else:
                del res[-1]

    if len(res) > 0:
        return False

    return True
