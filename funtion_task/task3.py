'''
Task 3: Write a function that takes in Multiply_number and multiply_upto argumenets where Muliply_number's multipilication table is
displayed untill multiply_upto

output->5x1=5
        5x2=10
        5x3=15


by default mulitply_upto should be 10 and multiply_number should be 1

'''

def table():
    a=int(input("enter multiply number : "))
    b=int(input("enter multiply up to number: "))
    if b<10:
        for number in range(1,11):
            print(f"{a} X {number}={a*number}")
    else:
        for number in range(1,b+1):
            print(f"{a} X {number}={a*number}")

table()
