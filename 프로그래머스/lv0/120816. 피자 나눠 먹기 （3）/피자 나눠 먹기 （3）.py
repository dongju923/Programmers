# n명의 사람이 최소 한 조각은 먹어야함
# 10명의 사람이 7조각의 피자를 한 조각씩 먹으면 3명이 못먹음 -> 나머지=3
def solution(slice, n):
    # n을 slice로 나눈 나머지가 0일때, 즉 피자조각이 안남을 때
    if n % slice == 0:
        # n을 slice로 나눈 몫을 반환
        return n // slice
    # n을 slice로 나눈 나머지가 0이 아닐때, 즉 피자조각이 남을 때
    elif n % slice != 0:
        # 한판을 더 시켜야 하므로 n을 slice로 나눈 몫에서 + 1
        return n // slice + 1
        