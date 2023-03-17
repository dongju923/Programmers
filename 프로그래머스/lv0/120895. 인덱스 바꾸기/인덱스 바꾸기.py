def solution(my_string, num1, num2):
    # 문자열 자체를 다른 값으로 할당이 불가하므로 리스트로 변형
    string = list(map(str, my_string))
    n1 = string[num1]
    n2 = string[num2]
    string[num1] = n2
    string[num2] = n1
    return ''.join(string)