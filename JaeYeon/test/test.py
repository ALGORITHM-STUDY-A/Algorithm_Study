def solution(numer1, denom1, numer2, denom2):
    answer = []

    answer.append(numer1 + numer2)
    answer.append(denom1, denom2)

    if answer[0] % answer[0] == 0:
        answer[0] == answer[0] // answer[1]
        answer[1] == answer[1] // answer[0]

    return answer

solution(1,2,3,4)