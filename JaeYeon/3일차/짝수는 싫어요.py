def solution(n):

    answer = []

    for i in range(1,n+1): # 인덱스가 아닌 실제값이 대입되어야하므로 인덱스는 1부터 n+1까지 들어가게 됩니다

        if i%2==0: # 짝수면 continue를 통해 다음 i로 넘어갑니다
            continue
        else:
            answer.append(i)
    return answer

print(solution(10))