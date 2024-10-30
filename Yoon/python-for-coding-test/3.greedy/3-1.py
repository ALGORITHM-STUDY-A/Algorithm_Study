# 3-1. 거스름돈

def charge(n):  # n은 거슬러줘야할 돈
    ans = 0  # 동전 개수를 담당

    if n // 500 != 0:  # 500원으로 거슬러 줄 수 있다면
        tmp = n  # tmp는 500원 개수를 위해 지정
        tmp //= 500

        n -= tmp * 500  # 일정 금액 거슬러주고 조정

        ans += tmp

    if n // 100 != 0:
        tmp = n
        tmp //= 100

        n -= tmp * 100

        ans += tmp

    if n // 50 != 0:
        tmp = n
        tmp //= 50

        n -= tmp * 50

        ans += tmp

    tmp = n
    tmp //= 10
    ans += tmp

    return ans


# 더 효율적인 풀이 법

def charge(n):

    coint_type = [500, 100, 50, 10] # 각 동전을 리스트로 지정
    count = 0   # 거슬러줄 동전 개수 (답)

    for coin in coin_types: # for문을 통해 코인 리스트에서 동전을 하나씩 채택
        count += n // coin  # 각 동전별로 개수 더하기 -> ex) 2500원을 500으로 나눈 몫은 5, 동전 개수 5개 발생

        n %= coin   # 거슬러준만큼 조정 -> ex) 25000을 500으로 나눈 나머지는 0



    return count
