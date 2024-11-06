def solution(n):

    ans=n//7
    re=n%7

    if re:
        ans+=1
    return ans
