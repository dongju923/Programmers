# filter -> 특정 조건에 맞는 값만 반환
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += 1
    return answer
    #return len(list(filter(lambda x: n % x == 0, range(1, n+1))))