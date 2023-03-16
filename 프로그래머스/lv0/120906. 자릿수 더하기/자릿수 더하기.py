# map(func, iterator) -> 반복가능한 객체에 func를 적용시킴
def solution(n):
    # n을 str객체로 만들고(iterator) int함수를 적용시킴 -> 리스트에 1, 2, 3, 4가 담김
    # sum()을 통해 리스트 내 원소의 합을 구해서 return
    return sum(list(map(int, str(n))))