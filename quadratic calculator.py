import random
aValue = int(input('what is your a value '))
bValue = int(input('what is your b value '))
cValue = int(input('what is your c value '))
multValue = aValue * cValue
addValue = bValue
factor1 = 0
factor2 = 0
while True:
    if factor1 + factor2 == addValue and factor1 * factor2 == multValue:
        break
    elif multValue < 0:
        factor1 = random.randint(multValue-1, -multValue+1)
        factor2 = random.randint(multValue-1, -multValue+1)
    elif multValue > 0:
        factor1 = random.randint(-multValue-1, multValue+1)
        factor2 = random.randint(-multValue-1, multValue+1)
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
print('(' + str(int(aValue/factor1Gcf)) + 'x' + neg + str(int(factor1/factor1Gcf)) + ')' + '(' + str(int(aValue/factor2Gcf)) + 'x' + neg2 + str(int(factor2/factor2Gcf)) + ')')



    
