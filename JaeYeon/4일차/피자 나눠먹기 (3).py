def solution(slice, n):

    ans=slice # 변하는 조각수를 저장하기 위해 변수 추가

    while ans//n<1: # 만약 인당 한 조각이 안나온다면
        ans+=slice # 조각수를 한 판만큼 추가 -> 사실상 한 판을 추가하는 것과 같다

    return ans//slice # 반복이 끝나면 ans로 나눠서 판수로 반환

print(solution(4,12))