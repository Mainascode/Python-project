# main.py
from auth import register_user, login_user
from services import add_client, view_clients, add_investment, view_investments

def main():
    logged_in_user = None

    while True:
        if not logged_in_user:
            print("\nWelcome to Financial Record CLI")
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            choice = input("Select an option: ")
            if choice == '1':
                username = input("Enter a username: ")
                password = input("Enter a password: ")
                logged_in_user = register_user(username, password)
            elif choice == '2':
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                logged_in_user = login_user(username, password)
            elif choice == '3':
                break
            else:
                print("Invalid option.")
        else:
            print("\nFinancial Record CLI")
            print("1. Add Client")
            print("2. View Clients")
            print("3. Add Investment")
            print("4. View Investments")
            print("5. Logout")

            choice = input("Select an option: ")
            if choice == '1':
                name = input("Enter client name: ")
                income = float(input("Enter client income: "))
                expenses = float(input("Enter client expenses: "))
                savings = float(input("Enter client savings: "))
                add_client(name, income, expenses, savings, logged_in_user.id)
            elif choice == '2':
                clients = view_clients(logged_in_user.id)
                for client in clients:
                    print(f"Client ID: {client.id}, Name: {client.name}")
            elif choice == '3':
                client_id = int(input("Enter client ID: "))
                type = input("Enter investment type: ")
                amount = float(input("Enter investment amount: "))
                add_investment(client_id, type, amount)
            elif choice == '4':
                investments = view_investments()
                for investment in investments:
                    print(f"Investment ID: {investment.id}, Type: {investment.type}, Amount: {investment.amount}")
            elif choice == '5':
                logged_in_user = None
                print("Logged out.")
            else:
                print("Invalid choice.")

if __name__ == '__main__':
    main()