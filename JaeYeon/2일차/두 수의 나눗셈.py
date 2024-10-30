def solution(num1, num2):

    # 두 수를 나눠서 1000으로 곱하고 1로 나누어 소수점을 제거한다
    return ((num1/num2)*1000)//1

def solutionV2(a,b):

    # 두 수를 나눠서 1000으로 곱한 후 int자료형으로 초기화 하여 소수점을 제거한다
    # 파이썬 자료형은 이렇게 쓰는거구나...
    return int((a/b)*1000)

print(solution(3,2))
print(solutionV2(3,2))