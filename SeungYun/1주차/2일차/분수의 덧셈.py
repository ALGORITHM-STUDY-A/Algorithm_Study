def gcd(a, b): #최대 공약수 구하는 함수입니당(유클리드 호제법), 라이브러리 쓸껄...
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + denom1 * numer2 #통분한 후 분자끼리 더함
    denom = denom1 * denom2 # 통분
    v = gcd(numer, denom) #더한 분수의 분자 분모 최대공약수
    return [numer // v, denom // v] #분자 분모의 최대 공약수로 각각 나눔
