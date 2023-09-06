def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]): 
        if p2.startswith(p1): #문자열이 특정 문자열로 시작하는지 확인
            return False
    return True