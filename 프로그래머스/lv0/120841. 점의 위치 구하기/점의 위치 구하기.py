def solution(dot):
    # 죄표 x, y가 둘다 양수일 때,
    if dot[0] > 0 and dot[1] > 0:
        return 1
    # x가 음수, y가 양수일 때,
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    # x, y가 둘다 음수일 때, 
    elif dot[0] < 0 and dot[1] < 0:
        return 3
    # x가 양수, y가 음수일 때,
    else:
        return 4