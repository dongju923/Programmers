def solution(n):
    answer = []
    for i in range(n+1):
        # 홀수인 것만 리스트에 담음
        if i%2 == 1:
            answer.append(i)
    return answer
    #return [i for i in range(n+1) if i % 2 == 1]