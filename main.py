
from auth import login, signup, load_fs
from task import add, view
from token_generator import load_token, remove_token

check_token = load_token()

def main():
    load_fs()
    print("Task Tracker")
    while True:
        choice = input("\n1. Login\n2. Signup\n3. Exit\nChoose an option: ")
        if choice == "1":
            session = login()
            if session:
                role, username, token = session
                if role == "admin" and check_token.get(username) == token:
                    admin_dashboard(role, username, token)
                elif role == "user" and check_token.get(username) == token:
                    user_dashboard(role, username, token)
                else:
                    print(f"Unknown role or token mismatch.")
                break
            else:
                print("Login failed")

        elif choice == "2":
            session = signup()
            if session:
                role, username, token = session
                if role == "admin" and check_token.get(username) == token:
                    admin_dashboard(role, username, token)
                elif role == "user" and check_token.get(username) == token:
                    user_dashboard(role, username, token)
                else:
                    print(f"Unknown role or token mismatch.")
                break

        elif choice == "3":
            print("Exiting.")
            break

        else:
            print("Invalid choice. Try again.")

def admin_dashboard(role, username, token):
    print(f"\nWelcome to the {role} dashboard.")
    print(f"Hello, {username}!")
    while True:
        check_token = load_token()
        choice = input("1. View Users\n2. Logout\nChoose an option: ")
        if choice == "1" and check_token.get(username) == token:
            print("Feature coming soon: View Users")
        elif choice == "2":
            remove_token(username)
            print("Logging out...")
            break
        else:
            print("Invalid choice.")

def user_dashboard(role, username, token):
    print(f"\nWelcome to the {role} dashboard.")
    print(f"Hello, {username}!")
    while True:
        choice = input("1. Add Task\n2. View Tasks\n3. Logout\nChoose an option: ")
        check_token = load_token()
        if choice == "1" and check_token.get(username) == token:
            add(username)
        elif choice == "2":
            view(username)
        elif choice == "3":
            remove = remove_token(username)
            print(f"{remove}")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

