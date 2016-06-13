"""A tiny dictionary to convert arabic numbers to their lexical counterparts"""

num = str(input("Enter a number:"))

numbers = dict()
numbers['1'] = 'one'
numbers['2'] = 'two'
numbers['3'] = 'three'
numbers['4'] = 'four'
numbers['5'] = 'five'
numbers['6'] = 'six'
numbers['7'] = 'seven'
numbers['8'] = 'eight'
numbers['9'] = 'nine'
numbers['10'] = 'ten'

print(numbers[num])
