#Business Logic and Services

# services.py
print("Services module loaded successfully!")

from models import Investment, session
from models import Client, session

def add_client(name, income, expenses, savings, user_id):
    """Add a new client to the database."""
    new_client = Client(name=name, income=income, expenses=expenses, savings=savings, user_id=user_id)
    session.add(new_client)
    session.commit()
    print("Client added successfully!")


def view_clients(user_id):
    """Retrieve and display all clients associated with a specific user."""
    clients = session.query(Client).filter(Client.user_id == user_id).all()
    return clients


def add_investment(client_id, investment_type, amount):
    """Add a new investment for a client."""
    new_investment = Investment(client_id=client_id, type=investment_type, amount=amount)
    session.add(new_investment)
    session.commit()
    print("Investment added successfully!")

def view_investments():
    investments = session.query(Investment).all()  # Adjust this query as needed for your model
    return investments


