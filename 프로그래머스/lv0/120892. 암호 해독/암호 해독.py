def solution(cipher, code):
    # 문자열내에서 code-1부터 시작해서 code만큼 건너뛴 값을 리턴
    # code-1부터 시작하는 이유는 인덱스가 0부터 시작하기 때문
    return cipher[code-1::code]