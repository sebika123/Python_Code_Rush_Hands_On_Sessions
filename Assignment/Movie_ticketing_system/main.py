import json
from art import *

class User:
    def __init__(self, username):
        self.username = username
        self.history = []

class Movie:
    def __init__(self, name, seats):
        self.name = name
        self.seats = seats

class TicketingSystem:
    def __init__(self):
        self.users = {}
        self.movies = {
            "Barbie": Movie("Barbie", {"1A": "Available", "2A": "Available", "2B": "Available"}),
            "Ant-Man": Movie("Ant-Man", {"1A": "Available", "2A": "Available", "2B": "Available"}),
            "Animal Jatra": Movie("Animal Jatra", {"1A": "Available", "2A": "Available", "2B": "Available"}),
            "The Nun": Movie("The Nun", {"1A": "Available", "2A": "Available", "2B": "Available"})
        }
        self.booked_seats = {}

    def load_data(self):
        try:
            with open('data/users.json', 'r') as f:
                self.users = json.load(f)
        except FileNotFoundError:
            pass
        
        try:
            with open('data/movies.json', 'r') as f:
                movies_data = json.load(f)
                for movie_name, movie_info in movies_data.items():
                    seats = movie_info['seats']
                    self.movies[movie_name] = Movie(movie_name, seats)
        except FileNotFoundError:
            pass

    def save_data(self):
        with open('data/users.json', 'w') as f:
            json.dump(self.users, f, indent=4)
        with open('data/movies.json', 'w') as f:
            movies_data = {movie.name: {'seats': movie.seats} for movie in self.movies.values()}
            json.dump(movies_data, f, indent=4)

    def sign_up(self, username):
        if username in self.users:
            print("Username already exists. Please choose another one.")
            return False
        else:
            self.users[username] = {'username': username, 'history': []}
            self.save_data()
            print("Sign up successful!")
            return True

    def book_ticket(self, username, movie_name, seat_number):
        if username not in self.users:
            print("Please sign up first.")
            return False
        
        if movie_name not in self.movies.keys():
            print("Movie not found.")
            return False
        movie = self.movies[movie_name]
        if seat_number not in movie.seats:
            print("Invalid seat number.")
            return False
        if movie.seats[seat_number] != 'Available':
            print("Seat already booked.")
            return False
        
        movie.seats[seat_number] = 'Booked'
        self.users[username]['history'].append({'movie': movie_name, 'seat': seat_number})
        self.booked_seats.setdefault(movie_name, []).append(seat_number)
        self.save_data()
        print("Ticket booked successfully!")
        return True

def main():
    ticketing_system = TicketingSystem()
    ticketing_system.load_data()
    tprint("Movie Ticketing System")
    while True:
        print("\n1. Sign up")
        print("2. Book Ticket")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter your username: ")
            ticketing_system.sign_up(username)
        elif choice == '2':
            username = input("Enter your username: ")
            if username not in ticketing_system.users:
                print("Please sign up first.")
                continue
            print("Available movies:")
            for movie_name in ticketing_system.movies.keys():
                print(movie_name)
            movie_name_input = input("Enter movie name: ").strip().lower()  
            movie_name = None
            for name in ticketing_system.movies:
                if name.lower() == movie_name_input:
                    movie_name = name
                    break
            if movie_name:
                if movie_name in ticketing_system.booked_seats:
                    available_seats = [seat for seat in ticketing_system.movies[movie_name].seats if
                                       ticketing_system.movies[movie_name].seats[seat] == "Available" and seat not in
                                       ticketing_system.booked_seats[movie_name]]
                else:
                    available_seats = [seat for seat in ticketing_system.movies[movie_name].seats if
                                       ticketing_system.movies[movie_name].seats[seat] == "Available"]
                if not available_seats:
                    print("Not available seats ")
                    continue
                print("Available seats:", ", ".join(available_seats))
                seat_number = input("Enter seat number: ")
                ticketing_system.book_ticket(username, movie_name, seat_number)
            else:
                print("Movie not found")
        elif choice == '3':
            print("Thank you.Keep Visiting")
            break
        else:
            print("Galat bho Please try again")


if __name__ == "__main__":
    main()
