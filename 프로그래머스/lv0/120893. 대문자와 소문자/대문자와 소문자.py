# swapcase() -> 대문자는 소문자로, 소문자는 대문자로 변경
def solution(my_string):
    answer =''
    for i in my_string:
        # i가 대문자이면
        if i.isupper():
            # 소문자로 변환후 문자열에 추가
            answer += i.lower()
        # i가 소문자이면
        else:
            # 대문자로 변환후 문자열에 추가
            answer += i.upper()
    return answer
    #return my_string.swapcase()
    