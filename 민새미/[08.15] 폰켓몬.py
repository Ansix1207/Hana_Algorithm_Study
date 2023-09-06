def solution(nums):
    answer = 0
    
    n=len(nums)/2
    # print(n)
    nums=set(nums)
    # print(nums)
    if n<len(nums):
        answer=n
    else:
        answer=len(nums)
    
    return answer