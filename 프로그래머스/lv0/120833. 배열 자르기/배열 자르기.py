# 리스트 슬라이스
# list[a:b] a부터 b까지 추출, b는 포함안됨
def solution(numbers, num1, num2):
    # num2의 인덱스도 포함시켜야 하므로 +1
    return numbers[num1:num2+1]