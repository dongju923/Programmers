def solution(hp):
    f = divmod(hp, 5)
    s = divmod(f[1], 3)
    return f[0] + s[0] + s[1]