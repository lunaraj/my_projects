import random
import sys
aValue = int(input('what is your a value '))
bValue = int(input('what is your b value '))
cValue = int(input('what is your c value '))
bozo = ''
if aValue < 0:
    aValue = -aValue
    bValue = -bValue
    cValue = -cValue
    bozo = '-'
multValue = aValue * cValue
addValue = bValue
factor1 = 0
factor2 = 0
guesses = 0
multiple = 0
if abs(aValue) < abs(bValue) and abs(aValue) < abs(cValue) :
    divisor = abs(aValue)
if abs(bValue) < abs(aValue) and abs(bValue) < abs(cValue) :
    divisor = abs(bValue)
if abs(cValue) < abs(aValue) and abs(cValue) < abs(bValue) :
    divisor = abs(cValue)
while divisor > 0:
    if aValue%divisor == 0 and bValue%divisor == 0 and cValue%divisor == 0:
        multiple = divisor
        break
    else:
        divisor -= 1
if multiple > 1:
    multiple = str(multiple)
else:
    multiple = ''
while True:
    if factor1 + factor2 == addValue and factor1 * factor2 == multValue:
        break
    elif multValue < 0:
        factor1 = random.randint(multValue-1, -multValue+1)
        factor2 = random.randint(multValue-1, -multValue+1)
        guesses+= 1
    elif multValue > 0:
        factor1 = random.randint(-multValue-1, multValue+1)
        factor2 = random.randint(-multValue-1, multValue+1)
        guesses += 1
    if guesses > 1000000:
        sys.exit('there are no integer values')
divisor = aValue
while divisor > 0:
    if aValue%divisor == 0 and factor1%divisor == 0:
        factor1Gcf = divisor
        break
    else:
        divisor -= 1
divisor = aValue
while divisor > 0:
    if aValue%divisor == 0 and factor2%divisor == 0:
        factor2Gcf = divisor
        break
    else:
        divisor -= 1
if factor1 < 0:
    neg = ''
else:
    neg = '+'
if factor2 < 0:
    neg2 = ''
else:
    neg2 = '+'
aValue2 = str(int(aValue/factor1Gcf))
aValue3 = str(int(aValue/factor2Gcf))
if aValue3 == '1':
    aValue3 = ''
if aValue2 == '1':
    aValue2 = ''
print(bozo + multiple + '(' + aValue2 + 'x' + neg + str(int(factor1/factor1Gcf)) + ')' + '(' + aValue3 + 'x' + neg2 + str(int(factor2/factor2Gcf)) + ')')


    
