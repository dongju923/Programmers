# 순서를 바꿔서 -> 모든 요소가 다 같아야함
# Counter -> 모든 요소와 개수를 딕셔너리 형태로 반환
from collections import Counter
def solution(before, after):
    # before와 after의 딕셔너리가 같으면 1반환 아니면 0반환
    return 1 if Counter(before) == Counter(after) else 0
    #return 1 if sorted(before)==sorted(after) else 0
    
    