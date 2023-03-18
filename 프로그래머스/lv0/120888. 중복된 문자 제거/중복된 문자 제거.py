# dict.fromkeys() -> 문자열을 딕셔너리 키로 만듦. 딕셔너리 키는 중복이 안됨
def solution(my_string):
    # 문자열을 딕셔너리의 키로 변환. 중복은 없어짐
    dic = dict.fromkeys(my_string)
    # dic의 키를 리스트에 담음
    li = list(dic.keys())
    # 리스트내 문자열을 join으로 문자열로 만듦
    return ''.join(li)
    #return ''.join(dict.fromkeys(my_string))
    
 """
def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer+=i
    return answer
 """
