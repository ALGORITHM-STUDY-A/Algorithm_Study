def solution(money):
    answer = []
    answer.append(money//5500) # 아아 개수
    answer.append(money%5500) # 잔돈
    return answer