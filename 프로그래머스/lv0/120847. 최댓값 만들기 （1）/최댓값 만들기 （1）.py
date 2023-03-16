# 가장 큰값 두개를 골라서 곱하면 됨
# 배열을 오름차순으로 정렬해서 리스트 인덱싱으로 맨 뒤에 값 두개를 곱하면 됨
def solution(numbers):
    numbers.sort()
    return numbers[-1]*numbers[-2]

