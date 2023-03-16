
def solution(array, height):
    count = 0
    for i in array:
        if i > height:
            count += 1
    return count

# 다른풀이
"""
def solution(array, height):
    # array에 height원소 추가
    array.append(height)
    # height보다 키가 큰사람을 구하는 것이 목표이므로 내림차순 정렬
    array.sort(reverse=True)
    # array내에서 height가 있는 인덱스 반환
    return array.index(height)
"""