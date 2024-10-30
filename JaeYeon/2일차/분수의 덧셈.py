import math


def solution(numer1, denom1, numer2, denom2):

    # 두 분수의 공통 분모를 계산
    # 공통 분모라기 보단 그냥 두 분모를 곱한 값을 나타내는 것 같다
    denominator = denom1 * denom2

    #그리고 분자도 그거에 맞게 곱해준다
    numerator = numer1 * denom2 + numer2 * denom1

    # 분자와 분모의 최대공약수를 구한다
    gcd = math.gcd(numerator, denominator)

    # 기약 분수로 만들기 위해 최대공약수로 나눈다
    return [numerator // gcd, denominator // gcd]