def solution(n):
    # 빈 리스트 만들기
    li = []
    # n값도 더해야 하므로 n+1만큼 반복
    for i in range(n+1):
        # i가 2로 나눠서 나머지가 0이면, 즉 짝수이면 리스트에 요소 추가
        if i % 2 == 0:
            li.append(i)
    # 리스트 요소를 다 더해서 반환
    return sum(li)
    
    # 한줄로 표현 가능
    # return sum([i for i in range(n+1) if i % 2 ==0])