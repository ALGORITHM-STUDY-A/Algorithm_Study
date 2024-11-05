def solution(price):
    if price>=500000: # 큰수부터 비교를 해야 코드를 간결하게 쓸 수 있기 때문에 50만원부터 비교
        price = price * 0.8 # 20퍼 할인
    elif price>=300000:
        price = price * 0.9 # 10퍼 할인
    elif price>=100000:
        price = price * 0.95 # 5퍼 할인
    return int(price)