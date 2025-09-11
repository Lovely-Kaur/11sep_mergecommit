database = {"user1": "pass123", "admin": "securepwd"}

username = input("Enter username: ")
password = input("Enter password: ")

if username in database and database[username] == password:
    print("Authentication successful!")
else:
    print("Invalid username or password.")
