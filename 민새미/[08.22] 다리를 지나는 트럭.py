def solution(bridge_length, weight, truck_weights):
    answer = 0
    ing = [0] * bridge_length
    while len(ing):
        answer += 1
        ing.pop(0)
        if truck_weights: #리스트가 비어있지 않을 때
            if sum(ing) + truck_weights[0] <= weight:
                ing.append(truck_weights.pop(0))
            else:
                ing.append(0)
    return answer

## 처음 코드 이렇게 짰음.. 당연히 틀렸음..ㅎ 중간 거쳐가는 다리를 모두 1칸이라고 생각을 해서 그랬던 것 같음
# 다음에는 다시 혼자 짜보려고 함.!!
def solution(bridge_length, weight, truck_weights):
    answer = 0
    ing=list()
    cnt=0
    end=list()
    
    x=truck_weights.pop(0)
    ing.append(x)
    cnt+=1
    while(1):
        if end==len(truck_weights):
            break
        
        if len(truck_weights)!=0:
            if sum(ing)+truck_weights[0]>weight or len(ing)+1 >bridge_length:
                k=ing.pop(0)
                end.append(k)
                cnt+=1

        else:
            k=ing.pop(0)
            end.append(k)
            cnt+=1
            print("여기?")
            print(cnt)
            break
                
        x=truck_weights.pop(0)
        ing.append(x)
        cnt+=1

        
    
    return answer