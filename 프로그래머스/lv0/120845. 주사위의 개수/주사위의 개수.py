# 상자의 가로가 10일때, 가로에만 3의 길이의 상자를 넣는 개수는 10 // 3, 즉 3개
# 상자의 세로가 8일때, 세로에만 3의 길이의 상자를 넣는 개수는 8 // 3, 즉 2개
# 상자의 높이가 6일때, 높이에만 3의 길이의 상자를 넣는 개수는 6 // 3, 즉 2개
# 몫을 다 곱하면 됨
def solution(box, n):
    answer = 1
    for i in box:
        answer *= i // n
    return answer