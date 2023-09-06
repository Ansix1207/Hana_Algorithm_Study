def solution(clothes):
    answer = 1

    d = dict()
    for i in range(len(clothes)):
        # key=clothes[i][1]
        # value=clothes[i][0]

        if clothes[i][1] in d:
            d[clothes[i][1]].append(clothes[i][0])
        else:
            d[clothes[i][1]] = [
                clothes[i][0]
            ]  # clothes[i][0]을 []로 안감싸면 문자열로 들어가지는것임 조심!!

    # print(d)

    for key in d.keys():
        answer = answer * (len(d[key]) + 1)

    # 출력 틀린 버전 (예외 출력이 무엇이 있을지는 모르겠음)
    #     x=1
    #     y=0
    #     for k in d.keys():
    #         if len(d.keys())==1:
    #             answer=len(d[k])
    #             return answer
    #         else:
    #             x*=len(d[k])
    #             y+=len(d[k])
    #         answer=x+y
    #         return answer

    return answer - 1
