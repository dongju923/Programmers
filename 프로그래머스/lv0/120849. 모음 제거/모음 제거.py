def solution(my_string):
    aeiou = ['a', 'i', 'e', 'o', 'u']
    return ''.join(list(map(lambda x: '' if x in aeiou else x, my_string)))


    
