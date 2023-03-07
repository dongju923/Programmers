# divmod(a, b) = a를 b로 나눈 몫과 나머지를 리스트로 반환
def solution(money):
    # 잔 수
    num = money // 5500
    # 거스름돈
    change = money % 5500
    return [num, change]
    #return divmod(money, 5500)