import numpy as np
def solution(n): 
    # 약수를 구해서 리스트에 담음
    answer = [i for i in range(1, n+1) if n % i == 0]
    # 약수의 개수가 홀수면 중앙에 있는 값의 제곱이 n과 같으므로 중앙값 먼저 구함
    mid = np.median(answer)
    # 중앙값의 제곱이 n과 같으면 1, 아니면 2반환
    if mid**2 == n:
        return 1
    else:
        return 2