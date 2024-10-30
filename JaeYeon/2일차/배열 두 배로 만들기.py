# 엄청난 발견, 하나의 파라미터로 여러개의 변수를 받으려면 (*파라미터) 하면 된다
# 하지만 이 문제에선 배열을 파라미터로 받으므로 저걸 쓸 필요가 없다

def solution(numbers):

    # 배열의 길이를 n으로 받고
    n=len(numbers)
    result=[]

    for i in range(n):

        # 배열의 인덱스의 값을 두 배로 곱하여 result 배열에 append
        result.append(numbers[i]*2)

    return result

print(solution([1,2,3]))
