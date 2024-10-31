# 10분 소모 / 정답

n = int(input())
m= list(input().split())

ans_x,ans_y = 1,1   # x가 행의 위치, y가 열의 위치

for direction in m: # 입력된 방법 다 시행

    if direction == "L" and ans_y > 1:  # 만약 1보다 같거나 작게되면 열의 위치를 벗어나간다
        ans_y -= 1
    elif direction == "R" and ans_y < n:    # 만약 n보다 같거나 크게 되면 열의 위치를 벗어나간다
        ans_y += 1
    elif direction == "U" and ans_x > 1:    # 만약 1보다 같거나 작게되면 행의 위치를 벗어나간다
        ans_x -= 1
    elif direction == "D" and ans_x < n:    # 만약 n보다 같거나 크게 되면 행의 위치를 벗어나간다
        ans_x += 1

print(ans_x, ans_y)

