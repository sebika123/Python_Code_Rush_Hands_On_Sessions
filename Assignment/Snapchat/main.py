# import json
# import os
# from art import *
# import getpass 

# def ensure_files():
#     if not os.path.exists('users.json'):
#         with open('users.json', 'w') as f:
#             json.dump({}, f)
#     if not os.path.exists('messages.json'):
#         with open('messages.json', 'w') as f:
#             json.dump({}, f)
 
# ensure_files()
 

# def load_data(filename):
#     with open(filename, 'r') as file:
#         return json.load(file)
 

# def save_data(filename, data):
#     with open(filename, 'w') as file:
#         json.dump(data, file, indent=4)
 

# def create_account():
#     users = load_data('users.json')
#     username = input("Enter your username: ")
#     if username in users:
#         print("Username already exists.")
#         return
#     password = input("Enter your password: ")
#     users[username] = {'password': password, 'messages': {}}
#     save_data('users.json', users)
#     print("Account created successfully!")
 

# def login():
#     users = load_data('users.json')
#     username = input("Username: ")
#     password = input("Password: ")
#     if username in users and users[username]['password'] == password:
#         print("Login successful.")
#         return username
#     else:
#         print("Invalid username or password.")
#         return None
 

# def send_message(sender):
#     receiver = input("Enter the username of the person you want to message: ")
#     message = input("Enter your message: ")
#     messages = load_data('messages.json')
 
#     # Ensure the sender has a messages entry
#     if sender not in messages:
#         messages[sender] = {}
 
#     # Ensure the conversation exists and limit the messages to 15
#     if receiver not in messages[sender]:
#         messages[sender][receiver] = []
#     messages[sender][receiver].append(message)
#     messages[sender][receiver] = messages[sender][receiver][-15:]
 
#     save_data('messages.json', messages)
#     print("Message sent.")
 

# def view_messages(username):
#     messages = load_data('messages.json')
#     for sender in messages:
#         for receiver in messages[sender]:
#             if receiver == username or sender == username:
#                 print(f"From {sender} to {receiver}: {messages[sender][receiver]}")

# def delete_message(username):
#     messages = load_data('messages.json')
#     print("\nYour conversations:")
#     for sender in messages:
#         for receiver in messages[sender]:
#             if receiver == username or sender == username:
#                 print(f"From {sender} to {receiver}")
 
#     sender = input("\nEnter the sender username: ")
#     receiver = input("Enter the receiver username: ")
#     if sender in messages and receiver in messages[sender]:
#         print("\nMessages in this conversation:")
#         for i, msg in enumerate(messages[sender][receiver], 1):
#             print(f"{i}. {msg}")
 
#         try:
#             msg_index = int(input("\nEnter the message index to delete: ")) - 1
#             if 0 <= msg_index < len(messages[sender][receiver]):
#                 del messages[sender][receiver][msg_index]
#                 save_data('messages.json', messages)
#                 print("Message deleted.")
#             else:
#                 print("Invalid message index.")
#         except ValueError:
#             print("Invalid input.")
#     else:
#         print("Conversation not found.")
 
# # Main function
# def main():
#     while True:
#         print("\n1. Create Account\n2. Login\n3. Send Message\n4. View Messages\n5. Delete Message\n6. Exit")
#         choice = input("Choose an option: ")
#         if choice == "1":
#             create_account()
#         elif choice == "2":
#             user = login()
#             if user:
#                 while True:
#                     print("\n1. Send Message\n2. View Messages\n3. Delete Message\n4. Logout")
#                     user_choice = input("Choose an option: ")
#                     if user_choice == "1":
#                         send_message(user)
#                     elif user_choice == "2":
#                         view_messages(user)
#                     elif user_choice == "3":
#                         delete_message(user)
#                     elif user_choice == "4":
#                         break
#                     else:
#                         print("Invalid choice.")
#         elif choice == "3":
#             print("Please login to send a message.")
#         elif choice == "4":
#             print("Please login to view messages.")
#         elif choice == "5":
#             print("Please login to delete a message.")
#         elif choice == "6":
#             break
#         else:
#             print("Invalid choice.")
 
# if __name__ == "__main__":
#     main()

import os
import json
from art import *
import getpass

class MessagingSystem:
    def __init__(self):
        self.ensure_files()

    def ensure_files(self):
        if not os.path.exists('users.json'):
            with open('users.json', 'w') as f:
                json.dump({}, f)
        if not os.path.exists('messages.json'):
            with open('messages.json', 'w') as f:
                json.dump({}, f)

    def load_data(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)

    def save_data(self, filename, data):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def create_account(self):
        users = self.load_data('users.json')
        username = input("Enter your username: ")
        if username in users:
            print("Username already exists.")
            return
        password = getpass.getpass("Enter your password: ")
        users[username] = {'password': password, 'messages': {}}
        self.save_data('users.json', users)
        print("Account created successfully!")

    def login(self):
        users = self.load_data('users.json')
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        if username in users and users[username]['password'] == password:
            print("Login successful.")
            return username
        else:
            print("Invalid username or password.")
            return None

    def send_message(self, sender):
        receiver = input("Enter the username of the person you want to message: ")
        message = input("Enter your message: ")
        messages = self.load_data('messages.json')
        if sender not in messages:
            messages[sender] = {}
        if receiver not in messages[sender]:
            messages[sender][receiver] = []
        messages[sender][receiver].append(message)
        messages[sender][receiver] = messages[sender][receiver][-15:]
        self.save_data('messages.json', messages)
        print("Message sent.")

    def view_messages(self, username):
        messages = self.load_data('messages.json')
        for sender in messages:
            for receiver in messages[sender]:
                if receiver == username or sender == username:
                    print(f"From {sender} to {receiver}: {messages[sender][receiver]}")

    def delete_message(self, username):
        messages = self.load_data('messages.json')
        print("\nYour conversations:")
        for sender in messages:
            for receiver in messages[sender]:
                if receiver == username or sender == username:
                    print(f"From {sender} to {receiver}")
        sender = input("\nEnter the sender username: ")
        receiver = input("Enter the receiver username: ")
        if sender in messages and receiver in messages[sender]:
            print("\nMessages in this conversation:")
            for i, msg in enumerate(messages[sender][receiver], 1):
                print(f"{i}. {msg}")
            try:
                msg_index = int(input("\nEnter the message index to delete: ")) - 1
                if 0 <= msg_index < len(messages[sender][receiver]):
                    del messages[sender][receiver][msg_index]
                    self.save_data('messages.json', messages)
                    print("Message deleted.")
                else:
                    print("Invalid message index.")
            except ValueError:
                print("Invalid input.")
        else:
            print("Conversation not found.")


def main():
    messaging_system = MessagingSystem()
    while True:
        tprint("Messaging System")
        print("\n1. Create Account\n2. Login\n3. Send Message\n4. View Messages\n5. Delete Message\n6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            messaging_system.create_account()
        elif choice == "2":
            user = messaging_system.login()
            if user:
                while True:
                    print("\n1. Send Message\n2. View Messages\n3. Delete Message\n4. Logout")
                    user_choice = input("Choose an option: ")
                    if user_choice == "1":
                        messaging_system.send_message(user)
                    elif user_choice == "2":
                        messaging_system.view_messages(user)
                    elif user_choice == "3":
                        messaging_system.delete_message(user)
                    elif user_choice == "4":
                        break
                    else:
                        print("Invalid choice.")
        elif choice == "3":
            print("Please login to send a message.")
        elif choice == "4":
            print("Please login to view messages.")
        elif choice == "5":
            print("Please login to delete a message.")
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
