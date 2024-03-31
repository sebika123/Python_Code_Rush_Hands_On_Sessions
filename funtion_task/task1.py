# Task 1: Create a function that takes in Principle time and Rate and returns SI 

def simple_interest():
    p=float(input('enter principle: '))
    t=float(input('enter time: '))
    r=float(input('enter rate: '))
    interest=(p*t*r)/100
    return interest

SI=simple_interest()
print("simple interest is ",SI)

