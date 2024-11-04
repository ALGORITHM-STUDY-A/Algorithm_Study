import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def solution(n):
    pieces_per_pizza = 6
    # 피자 조각 수와 사람 수 n의 최소 공배수 구하기
    lcm_pieces = lcm(pieces_per_pizza, n)
    # 최소 공배수를 피자 조각 수로 나누어 피자 판 수를 구하기
    return lcm_pieces // pieces_per_pizza


"""

해당 문제는 최소공배수를 이용해서 푸는 문제였습니다
n명이 먹어야하는 조각 수를 최소공배수를 이용하여 구한 후
이 조각 수를 피자 판 수로 바꾸어 출력하면 되는 것이었습니다

파이썬 3.9 이상에서는 최소공배수를 구하는 모듈이 지원이 되었지만,
우리가 사용하는 3.7은 최대공약수만 지원하기 때문에 a,b를 추가로 곱해서 최소공배수를 구합니다

어떨때 gcd,lcm을 사용할까?
두개의 변수의 나누기를 통한 공통변수를 찾는다 -> gcd
두개의 변수의 배수를 통한 공통변수를 찾는다 -> lcm

"""