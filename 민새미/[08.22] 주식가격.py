def solution(prices):
    answer = []
    
    arr=[]
    cnt=0
    for i in range(len(prices)):
        k=prices[i]
        for j in range(i, len(prices)-1):
            if k> prices[j]: #기준 값보다 가격이 떨어질 경우! , 가격이 떨어지지 않는 기간동안의 초니까 알아야하니까
                break
            cnt+=1
        answer.append(cnt)
        cnt=0    
    return answer