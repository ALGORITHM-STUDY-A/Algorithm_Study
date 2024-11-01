# 2분 소모 / 정답

n, k = map(int, input().split())    # n,k 값 입력받기

ans = 0

while n!=1: # n이 1이 될때까지 반복
    if n%k==0:  # 만약 n이 나누어 떨어지면 2번 방법
        n /= k  # n을 k로 나누어주기
        ans += 1    # 횟수 +1
    else:
        n -= 1  # 그 외에는 1번 방법
        ans +=1 # 횟수 +1

print(ans)

