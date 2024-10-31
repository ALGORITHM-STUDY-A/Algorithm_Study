# 큰 수의 법칙
# 제한시간: 30분 / 2019 국가 교육기관 코딩 테스트 기출 / 12분 소모 / 정답

n,m,k = map(int,input().split())    #   첫째줄에 n,m,k가 공백으로 구분해서 입력

n_list = list(map(int,input().split()))   # 둘째줄에 n개의 자연수가 주어진다. 자연수는 공백으로 구분

n_list.sort()


temp = 0  # 연달아 더해지는 횟수 체크

ans = 0

for _ in range(m):  # m번 더해지기만 하면 되서 가운데 _

    if temp != k:
        ans += n_list[len(n_list) - 1]    # 오름차순 정렬을 했기에 마지막 수가 제일 크므로 마지막 수 더해주기(인덱스니 길이에 1 빼기)
        temp += 1

    else:
        ans += n_list[len(n_list) - 2]    # 연속으로 더해지는 횟수가 되었을 경우 제일 큰수보다 하나 작은 수 더해주고 연달아 더해진 횟수 초기화
        temp = 0


print(ans)





