def solution(my_string):
    answer = []
    for i in my_string:
        # i가 숫자일때,
        if i.isnumeric():
            # i를 리스트에 담음
            answer.append(i)
    # 리스트를 오름차순으로 정렬
    answer.sort()
    # 리스트 내 문자열을 int로 변환후 return
    return list(map(int, answer))
    #return list(map(int, sorted([i for i in my_string if i.isnumeric()])))