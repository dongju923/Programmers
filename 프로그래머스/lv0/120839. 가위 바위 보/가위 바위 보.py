def solution(rsp):
    # 0일때 5, 2일때 0, 5일때 2를 내면되므로, 딕셔너리로 저장
    dic = {'0' : '5', '2' : '0', '5' : '2'}
    # rsp를 반복해서 딕셔너리의 key값으로 넣고 value를 출력
    return ''.join([dic.get(i) for i in rsp])