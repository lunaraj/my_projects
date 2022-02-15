balance = float(input('balance = '))
annualInterestRate = float(input('annual interest rate = '))
mir = annualInterestRate/12
bal = balance
count = 12
mplb = balance/12
mpub = (balance*(1+mir)**12)/12
lmp = (mplb+mpub)/2
epsilon = 0.01
while True:
    bal = balance
    count = 12
    while count > 0:
        bal -= lmp
        bal += bal*mir
        count -= 1
    if abs(bal) <= epsilon:
        break
    else:
        print(lmp)       
        if bal < 0:
            mpub = lmp
        elif bal > 0:
            mplb = lmp
print('Lowest Payment: ' + str(lmp))


    

    
