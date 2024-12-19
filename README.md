# Python-project
# Financial Records CLI

## Overview

The Financial Records CLI is a command-line interface application designed to help users manage financial data efficiently. Users can register, log in, manage client records, add investments.

This application is built using Python and leverages SQLAlchemy for database operations.

---

## Features

1. **User Authentication**:
    - User registration
    - Login functionality
    

2. **Client Management**:
    - Add client information (name, income, expenses, savings).
    - View all clients and their details.

3. **Investment Management**:
    - Add investments for clients.
    - View all investments.

---

## Prerequisites

Ensure you have the following installed:

- Python 3.8 or later
- Virtualenv (optional but recommended)

---

## Setup

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create and Activate Virtual Environment** (optional):
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows: .\env\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Setup Database**:
    - Ensure the database configuration in your project is correct (e.g., SQLite URL).
    - Run migrations if applicable.

---

## Usage

Run the CLI application using:

```bash
python main.py
```

### Commands:

- **Register**: Create a new user.
- **Login**: Log into your account.
- **Add Client**: Add details of a financial client.
- **View Clients**: Display all clients.
- **Add Investment**: Log investments for a specific client.
- **View Investments**: Display all recorded investments.
- **Logout**: End the session.

---

## Directory Structure

```
.
|-- main.py                # Entry point of the application
|-- auth.py                # User authentication module
|-- services.py            # Business logic for managing clients and investments
|-- models.py              # Database models
|-- requirements.txt       # Project dependencies
|-- README.md              # Project documentation
```

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

