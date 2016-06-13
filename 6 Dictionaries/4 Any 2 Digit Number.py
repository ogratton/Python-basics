r = 0
        
while r<1:
    try:
        num = int(input("Enter a number (not the word):"))

        numbers = dict()
        numbers['0'] = 'zero'
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
        numbers['20'] = 'twenty'
        numbers['30'] = 'thirty'
        numbers['40'] = 'forty'
        numbers['50'] = 'fifty'
        numbers['60'] = 'sixty'
        numbers['70'] = 'seventy'
        numbers['80'] = 'eighty'
        numbers['90'] = 'ninety'
        numbers['100'] = 'one hundred'

        num2 = str(num)

        print(numbers[num2])

    except ValueError:
        print("I can't do that one")


    
