# 풀이

# 구현에서 실수가 많은 문제
# 포인트는 가장 큰수 그리고 그 다음으로 큰 수만 알면 된다

n,m,k = map(int,input().split())

# 제일 첫 실행에서 실수한 부분
# 입력값을 list로 사용할려면 list()로 감싸줘야하는데 까먹었다.
data = list(map(int,input().split()))

data.sort() # 정렬
first = data[n-1]
second = data[n-2]

# 여기서 생각이 든게 내림차순을 활용해서 0번인덱스 1번인덱스를 꺼내도 되었는데 그걸 까먹었다.

# data.sort(reverse = True) -> sort() 안에 조건 reverse = True를 넣어 내림차순을 만들 수 있다
# first = data[0]
# second = data[1]

result = 0

while True: # 나는 더해지는 횟수를 통한 for문을 사용했지만 답안 예시에서는 조금 상이했다
    for i in range(k):  # 연속으로 더해질수 있는만큼 for 문을 통해 더하고
        if m == 0:  # 만약 더하는 횟수가 다 되었다면 break
            break
        result += first
        m -= 1  # 실행이 되면 한번 더 했으니 -1
    if m == 0:
        break

    result += second    # 만약 더한 횟수가 됐으면 두번째로 큰수 더하기
    m -= 1
