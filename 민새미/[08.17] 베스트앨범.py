# 참고해서 품 -> 내가 생각한 로직이랑 거의 비슷함.
# 근데 여기서 중요했던 점은 sorted(~, key=lambda)람다를 써서 정렬순을 정하는것이었음!!!!!!1
def solution(genres, plays):
    answer = []
    tmp = list()
    d = dict()

    # tmp=[[genres[i], plays[i], i] for i in range(len(genres))]
    for i in range(len(genres)):
        tmp.append([genres[i], plays[i], i])
    tmp = sorted(tmp, key=lambda x: (x[0], -x[1], x[2]))

    #     for g in tmp:
    #         print(g)
    #         if g[0] not in d:
    #             d[g[0]]=g[1]
    #         else:
    #             d[g[0]] +=g[1]
    for i in range(len(tmp)):
        if tmp[i][0] not in d:
            d[tmp[i][0]] = tmp[i][1]
        else:
            d[tmp[i][0]] += tmp[i][1]
    d = sorted(d.items(), key=lambda x: -x[1])

    # for i in d:
    #     count=0
    #     for j in tmp:
    #         if i[0]==j[0]:
    #             count+=1
    #             if count>2:
    #                 break
    #             else:
    #                 answer.append(j[2])
    for i in range(len(d)):
        count = 0
        for j in range(len(tmp)):
            if d[i][0] == tmp[j][0]:
                count += 1
                if count > 2:
                    break
                else:
                    answer.append(tmp[j][2])

    return answer


# 딕셔너리를 2개 사용하여 작성한 다른 코드
def solution(genres, plays):
    answer = []
    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for k, v in sorted(dic2.items(), key=lambda x: x[1], reverse=True):
        for i, p in sorted(dic1[k], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(i)

    return answer


# 처음 작성한 코드이면서 테케만 통과했지 히든테케에서 13퍼 정답률ㅋㅎ 그래서 틀린 코드임..
def solution(genres, plays):
    answer = []
    d = dict()
    for i in range(len(genres)):
        if genres[i] in d:
            d[genres[i]].append(plays[i])
        else:
            d[genres[i]] = [plays[i]]
    dd = dict()
    c = list()
    for i in range(len(genres)):
        dd[plays[i]] = genres[i]
    for i in sorted(plays, reverse=1):
        c.append(dd.get(i))

    c = list(set(c))
    cnt = 0
    for i in range(len(c)):
        p = max(d.keys())
        d.get(p).sort()
        for j in range(len(d.get(p)) - 1, -1, -1):
            answer.append(plays.index(d.get(p)[j]))
            cnt += 1
            if cnt == 2:
                del d[p]
                cnt = 0
                c.remove(p)
                break

    return answer
