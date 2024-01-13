def login():
    # Hardcoded username and password for simplicity
    hardcoded_username = "user"
    hardcoded_password = "password"

    # Get user input for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the entered username and password match the hardcoded values
    if username == hardcoded_username and password == hardcoded_password:
        print("Login successful!")
    else:
        print("Invalid credentials. Please try again.")

# Call the login function
login()
