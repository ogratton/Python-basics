r = 0

while r<1:

    a = " and "
    space = ""
    
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
    numbers['200'] = 'two hundred'
    numbers['300'] = 'three hundred'
    numbers['400'] = 'four hundred'
    numbers['500'] = 'five hundred'
    numbers['600'] = 'six hundred'
    numbers['700'] = 'seven hundred'
    numbers['800'] = 'eight hundred'
    numbers['900'] = 'nine hundred'

    num2 = str(num)                                                 # num2 is the string counterpart of num

    if len(num2) == 1:                                              # if the number is one digit long...
        onedigit = numbers[num2]                                    # the output is the translation of num2 (i.e. straightforward translation)
        print(onedigit)                                             # print it
        
    elif len(num2) == 2:                                            # if the number is two digits long...
        if 11 <=num <=19:                                           # and if it is a number between 11 and 19 (irregular numbers)
            print(numbers[num2])                                    # print a straightforward translation (as irregulars are in the dictionary)
            
        else:                                                       # if the number is two digits long and bigger than 19...      
            num3 = ((num//10)*10)                                   # num3 is this thing (mathematical "trick" to isolate the "ten"s)
            num4 = str(num3)                                        # num4 is the string counterpart of num3 (so that they can be printed)
            num5 = str(num-num3)                                    # num5 is the string of num-num3 (the "unit" (e.g. in 45, 40=tens, 5=units)
            num6 = int(num5)                                        # num6 is the integer is num5
            
            if num6 == 0:                                           # if the number ends in a zero...
                num5 = "no"                                         # translate it as "no" (which translates to a blank)
            else:                                                   # else...
                num5 = num5                                         # don't bother

            twodigits = (numbers[num4])+ " " + (numbers[num5])      # output is the ten plus the unit
            print(twodigits)                                        # print it
            
    elif len(num2) == 3:                                            # if the number is 3 digits longs

        num3 = ((num//100)*100)                                     # num3 is this thing (mathematical "trick" to isolate the "hundred"s)
        num4 = (((num-num3)//10)*10)                                # num4 is this thing (mathematical "trick" to isolate the "ten"s)
        num5 = (num-num3-num4)                                      # num5 is the "unit"
        num6 = str(num3)
        num7 = str(num4)                                            # these 3 lines convert the numbers to strings for printing
        num8 = str(num5)
        num9 = (num-num3)                                           # e.g. 145-100 = 45. this is for identifying teens
        num10 = str(num9)                                           # string of num9 (again for printing)
        
        if 11 <=num9 <20:                                           # if it's a teen
            threedigitteen = (numbers[num6] + " and " + numbers[num10])
            print(threedigitteen)                                   # print "hundred" "and" "teen"

        else:

            if num4 == 0:                                           # if it's 100 to 109
                num7 = "no"                                         # don't say the zero
            else:                                                   # else...
                num7 = num7                                         # do nothing

            if num4 >= 1:                                           # if the tens are bigger than or equal to 1
                space = " "                                         # set space to actually have a space in it
            else:                                                   # else...
                num7 = num7                                         # do nothing
                
            if num5 == 0:                                           # if it ends in 0
                if num4 == 0:                                       # and if the "ten" is 0 too (ergo it is 100,200,300 etc.)
                    num8 = "no"                                     # don't print the "zero" at the end
                    a = ""                                          # don't say and at the end
                    space = " "                                     # put the space in
                else:                                               # else...
                    num8 = "no"                                     # change num8 but don't touch and and space
            else:                                                   # if both are false...
                num8 = num8                                         # do nothing

            threedigits = (numbers[num6])+ a + (numbers[num7]) + space + (numbers[num8])
            print(threedigits)                                      # output  
        

    
