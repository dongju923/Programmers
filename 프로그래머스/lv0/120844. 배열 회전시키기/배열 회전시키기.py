def solution(numbers, direction):
    if direction == 'right':
        return [numbers[-1]] + numbers[0:-1]
    else:
        return numbers[1:] + [numbers[0]]
    #return [numbers[-1]] + numbers[0:-1] if direction=='right' else numbers[1:] + [numbers[0]]