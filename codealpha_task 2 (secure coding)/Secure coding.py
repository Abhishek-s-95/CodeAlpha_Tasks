import hashlib

stored_user = "admin"
stored_pass = hashlib.sha256("admin123".encode()).hexdigest()

username = input("Enter username: ")
password = input("Enter password: ")

hashed_input = hashlib.sha256(password.encode()).hexdigest()

if username == stored_user and hashed_input == stored_pass:
    print("Login successful")
else:
    print("Access denied")
