# len(): 원소의 길이 출력
def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer
    # retrun [len(i) for i in strlist]