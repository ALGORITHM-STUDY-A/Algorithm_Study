def solution(numbers):

    n=len(numbers) # 반복을 위해 배열의 길이를 받고
    answer=0

    for i in range(n):
        answer+=numbers[i] # 배열의 숫자를 answer에 저장해서

    return answer/n # 평균을 리턴