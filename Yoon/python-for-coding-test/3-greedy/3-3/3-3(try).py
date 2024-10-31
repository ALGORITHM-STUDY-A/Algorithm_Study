# 7분 소모 / 정답

n,m = map(int, input().split()) # n,m 입력 받기

# 리스트 컴프리헨션
# 행,열이 구현되어야 하기 위해 이차원리스트 구현
# 입력값을 리스트로 받고 그걸 행의 개수만큼 반복하여 리스트 구현
data = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):  # 첫번째 행부터 마지막 행까지 반복을 위해

    if ans < min(data[i]):  # 해당 행에 최소값을 꺼내오기 + 기존값보다 크면 교체
        ans = min(data[i])

print(ans)



