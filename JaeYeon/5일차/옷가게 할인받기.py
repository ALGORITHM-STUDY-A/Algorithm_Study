def solution(price):

    sale=0

    if 300000>price>100000:
        sale=0.05
    elif 500000>price>=300000:
        sale=0.1
    elif price>=500000:
        sale=0.2

    price=int(price-(price*sale))

    return price

print(solution(580000))  # 예상 결과: 464000 (580000 - 20% 할인)
print(solution(120000))  # 예상 결과: 114000 (120000 - 5% 할인)
print(solution(300000))  # 예상 결과: 270000 (300000 - 10% 할인)
print(solution(500000))  # 예상 결과: 400000 (500000 - 20% 할인)






def solution2(price):
    if price >= 500000:
        sale = 0.2
    elif price >= 300000:
        sale = 0.1
    elif price >= 100000:
        sale = 0.05
    else:
        sale = 0

    price = int(price * (1 - sale))
    return price

print(solution2(580000))  # 예상 결과: 464000 (580000 - 20% 할인)
print(solution2(120000))  # 예상 결과: 114000 (120000 - 5% 할인)
print(solution2(300000))  # 예상 결과: 270000 (300000 - 10% 할인)
print(solution2(500000))  # 예상 결과: 400000 (500000 - 20% 할인)