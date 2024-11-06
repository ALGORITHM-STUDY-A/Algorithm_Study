def solution(array):
    answer = 0

    n=len(array)
    watch={}

    for i in range(n):

        watch[array[i]]+=1
        a=watch[array[i]]

        if a>answer:
            answer=a


    v=len(watch)

    for i in watch:
        if i==answer:
            continue
        elif watch[answer]==watch[i]:
            return -1

    return answer


def solutionV2(array):
    # 각 숫자의 출현 횟수를 세기 위한 딕셔너리
    watch = {}

    # 출현 횟수 세기
    for num in array:
        if num in watch:
            watch[num] += 1
        else:
            watch[num] = 1

    # 최대 출현 횟수 및 후보 찾기
    max_count = max(watch.values())
    mode_candidates = [num for num, count in watch.items() if count == max_count]

    # 후보가 여러 개일 경우 -1 반환
    if len(mode_candidates) > 1:
        return -1

    return mode_candidates[0]
print(solution([1,2,3,3,3,4]))

"""
1. 리스트에서 변수를 가져옵니다
2. 해당 변수에 대한 값을 +1 합니다
    - 딕셔너리로 구현하면 될 듯 합니다
3. 그걸 반복하고
4. 끝에 값이 제일 큰 값을 리턴합니다
"""