def solution(n, t):
    # 1시간에 두배만큼 증식 -> t시간에는 2^t만큼 증식
    # 처음 세균마리수가 n이므로 2^t*n
    return 2**t*n