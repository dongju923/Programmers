# 합성수: 1보다 큰 자연수 중 소수가 아니고 약수의 개수가 세개 이상인 수
def solution(n):
    li = []
    cnt = 0
    # 1보다 커야하므로 2부터 반복 시작
    for i in range(2, n+1):
        # 약수를 구하기 위한 반복
        for j in range(1, n+1):
            # print(i, j)
            if i % j == 0:
                li.append(i)
        # 약수의 개수가 3개 이상이면 cnt를 1씩 증가
        if li.count(i) >= 3:
            cnt+=1        
    return cnt