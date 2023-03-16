# isdigit() -> 문자열이 숫자인지 판별함. True, False반환
def solution(my_string):
    return sum([int(i) for i in my_string if i.isdigit()])