def solution(numbers, direction):
    if direction == 'right':
        # 맨 뒤값을 맨 앞으로 보내고, 나머지를 그대로
        return [numbers[-1]] + numbers[0:-1]
    else:
        # 맨 앞값을 뒤로 보내고, 나머지를 그대로
        return numbers[1:] + [numbers[0]]
    #return [numbers[-1]] + numbers[0:-1] if direction=='right' else numbers[1:] + [numbers[0]]
