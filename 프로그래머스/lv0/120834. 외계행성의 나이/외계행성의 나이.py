def solution(age):
    alphabet = ['a','b','c','d','e','f','g','h','i','j']
    answer = []
    for i in list(map(int, str(age))):
        answer.append(alphabet[i])
    return ''.join(answer)