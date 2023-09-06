# 이 문제는 완탐인가? 그런것 같음 -> 선형 구조인가 비선형 구조인가? 내 생각에는 비선형 구조 같음.. -> 잘 접근했나 확인하니... DP로 푸는 문제였음.. 왜..?
# 이 문제는 DP로 풀어보자 작은 문제들이 여러 번 반복되는가를 찾아보자.-> 상향식 방식인가, 하향식 방식인가? -> 

#1을 2개 산 값과 2를 1개 산 값을 비교해서 최댓값을 저장해놓음..!
#자세한 설명은 노타빌리티에 작성함.
# DP에서 가장 중요하게 생각하는 부분이 초기화 하여 쓰는 arr 배열의 의미라는 것이다. arr[1] 이 의미하는 것은 카드 1개를 구매하고 싶을때 가장 비싸게 계산된 금액이라는 것이다.
# arr[2]는 카드 2개를 구매하고 싶을때 가장 비싸게 계산된 금액을 넣어주는 것!!이다!

n=int(input())
cards=[0]
cards+=list(map(int, input().split()))

print(cards)

def dp(n):
    arr=[0]*(n+1)
    # arr[1]=cards[1]

    # if n<2:
    #     return arr[n]
    # for i in range(2, n+1):
    #     arr[i]=max(arr[i-1]+arr[i-2],cards[i])

#이렇게 계속 하다가 이중 for문일까.. 생각만 하고 안해봄.. 결국 코드 참고해서 문제 풀었음.


    for i in range(1, n+1):
        for j in range(1, i+1): #여기서 i번 반복함!
            arr[i]=max(arr[i], arr[i-j]+cards[j])


        
    print(arr)
    return arr[n]

print(dp(n))