def solution(my_string):
    answer = ''
    for i in my_string:
        answer += i.lower()
        answer = sorted(answer)
    return ''.join(answer)
    #return ''.join(sorted(my_string.lower())