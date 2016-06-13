r = 0

while r<1:
    num = int(input("Enter a number (not the word):"))

    numbers = dict()
    
    numbers['no'] = ''
    
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
    
    numbers['11'] = 'eleven'
    numbers['12'] = 'twelve'
    numbers['13'] = 'thirteen'
    numbers['14'] = 'fourteen'
    numbers['15'] = 'fifteen'
    numbers['16'] = 'sixteen'
    numbers['17'] = 'seventeen'
    numbers['18'] = 'eighteen'
    numbers['19'] = 'nineteen'
    
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

    if len(num2) == 1:
        num3 = num2
        onedigit = numbers[num2]
        print(onedigit)
        
    elif len(num2) == 2:
        if 11 <=num <20:
            print(numbers[num2])
            
        else:
                
            num3 = ((num//10)*10)
            num4 = str(num3)
            num5 = str(num-num3)
            num6 = int(num4)
            
            if num6 == 0:
                num5 = "no"
            else:
                num5 = num5

            twodigits = (numbers[num4])+ " " + (numbers[num5])
            print(twodigits)
            
    else:
        print(numbers[num2])
        

    
