# Task 2: Make it such that the function doesn't return SI just displays it 

def simple_interest():
    p=float(input('enter principle: '))
    t=float(input('enter time: '))
    r=float(input('enter rate: '))
    interest=(p*t*r)/100
    print (interest)

simple_interest()
