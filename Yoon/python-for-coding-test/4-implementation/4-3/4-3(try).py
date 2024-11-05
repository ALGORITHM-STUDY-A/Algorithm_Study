# 21분 소모 / 정답

n = str(input())

data = list(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] for _ in range(8))

n_column = int(n[1]) - 1
n_row = data[0].index(n[0])

ans = 0

temp_c = n_column
temp_r = n_row

# 8가지의 경우의 수 확인

if temp_c + 2 <= 7 and temp_r + 1 <= 7:
    ans += 1
if temp_c + 2 <= 7 and temp_r - 1 >= 0:
    ans += 1
if temp_c - 2 >= 0 and temp_r + 1 <= 7:
    ans += 1
if temp_c - 2 >= 0 and temp_r - 1 >= 0:
    ans += 1

if temp_c + 1 <= 7 and temp_r + 2 <= 7:
    ans += 1
if temp_c - 1 >= 0 and temp_r + 2 <= 7:
    ans += 1
if temp_c + 1 <= 7 and temp_r - 2 >= 0:
    ans += 1
if temp_c - 1 >= 0 and temp_r - 2 >= 0:
    ans += 1

print(ans)