def solution(n):
    slice = 6
    # 모두 같은 수의 피자 조각을 먹지 못하면 반복
    while(slice%n != 0):
        # 6조각을 추가로 더함
        slice += 6
    # 총 조각에서 6으로 나눈 몫을 리턴
    return slice // 6