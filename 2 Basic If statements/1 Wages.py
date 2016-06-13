def calcWeeklyWages(totalHours, hourlyWage):
    '''Return the total weekly wages for a worker working totalHours,
    with a given regular hourlyWage.  Include overtime for hours over 40.
    '''
    if totalHours <= 40:
        totalWages = hourlyWage*totalHours
    else:
        overtime = totalHours - 40
        totalWages = hourlyWage*40 + (1.5*hourlyWage)*overtime
    return totalWages

def main():
    hours = float(input('Enter hours worked per week: '))
    wage = float(input('Enter wage per hour: '))
    total = calcWeeklyWages(hours, wage)
    print('Wages for {hours} hours at ${wage:.2f} per hour are ${total:.2f} including overtime.'
          .format(**locals()))

main()

import os
os.system("pause")	
