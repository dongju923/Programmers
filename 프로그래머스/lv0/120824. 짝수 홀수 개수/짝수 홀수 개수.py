def solution(num_list):
    # 짝수
    even = [i for i in num_list if i%2 ==0]
    # 홀수
    odd = [i for i in num_list if i%2 ==1]
    return len(even), len(odd)