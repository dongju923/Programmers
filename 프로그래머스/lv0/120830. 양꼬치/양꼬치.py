def solution(n, k):
    service = n // 10
    return 12000* n + (k - service) * 2000
    # return 12000 * n + (k - n//10) * 2000