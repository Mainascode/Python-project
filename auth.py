# auth.py
import bcrypt
from models import User, session

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def register_user(username, password):
    if session.query(User).filter_by(username=username).first():
        print("Username already exists.")
        return None

    hashed_password = hash_password(password)
    new_user = User(username=username, password=hashed_password)
    session.add(new_user)
    session.commit()
    print("User registered successfully!")
    return new_user

def login_user(username, password):
    user = session.query(User).filter_by(username=username).first()
    if not user:
        print("User not found.")
        return None

    if not verify_password(password, user.password):
        print("Invalid password.")
        return None

    print(f"Welcome, {username}!")
    return user
