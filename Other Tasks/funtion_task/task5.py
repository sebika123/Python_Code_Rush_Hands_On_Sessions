'''
Task 5: Create a function that takes in username, password ,DOB,phone_number,from user and creates a dictionary from it with and without using kwargs
'''

def create_user_dict_with_kwargs(**kwargs):
    return kwargs

# Example usage:
username = input("enter username: ")
password = input("enter password: ")
dob = input("enter date of birth (YYYY-MM-DD): ")
phone_number = input("enter phone number: ")

user_info = create_user_dict_with_kwargs(username=username, password=password, dob=dob, phone_number=phone_number)
print("user dictionary:", user_info)
