import hashlib

stored_user = "admin"
stored_pass = hashlib.sha256("admin123".encode()).hexdigest()

max_attempts = 3
attempts = 0

while attempts < max_attempts:

    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed_input = hashlib.sha256(password.encode()).hexdigest()

    if username == stored_user and hashed_input == stored_pass:
        print("Login successful")
        break
    else:
        attempts += 1
        print("Invalid credentials")
        print("Attempts left:", max_attempts - attempts)

if attempts == max_attempts:
    print("Maximum login attempts reached. Access blocked.")
