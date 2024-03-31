'''
Task 4: Create a function which takes in N number of variables and returns their sum (N=random)
'''
def sum_of_n_numbers(*numbers_tuple):
    return sum(list(numbers_tuple))

total=sum_of_n_numbers(1,2,3,4,5)
print (total)