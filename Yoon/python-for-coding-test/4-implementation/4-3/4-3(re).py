# 21분 + 7분 / 정답

n = str(input())    # 입력이 a1 이런식으로 주어진다

# 가로가 알파벳 세로가 숫자로 8*8
# 그렇다면 행 정보가 숫자, 열 정보가 문자인 셈

alpha = ['a','b','c','d','e','f','g','h']

n_c = int(n[1]) - 1  # 뒤에 숫자정보가 행 정보니 column에 추가, 인덱스상 시작은 0이기에 -1을 통한 조율
n_r = alpha.index((n[0])) # 앞에 알파벳 정보(열 정보 row)를 미리 만들어둔 리스트에서 인덱스 정보 가져오기
ans = 0
# 8가지 방법을 리스트로 구현

direc = [[-1,2],[-1,-2],[1,2],[1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]

# 8가지 방법 확인
for d in direc:
    d_c = n_c + d[0]
    d_r = n_r + d[1]

    # 체스판을 벗어나지 않는다면 +1
    if 0<=d_c<=7 and 0<=d_r<=7:
        ans +=1


print(ans)