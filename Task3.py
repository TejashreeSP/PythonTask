import hashlib

# Dictionary to store username and hashed password
users = {}

# Function to hash a password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register function
def register(username, password):
    if username in users:
        return "User already exists"
    users[username] = hash_password(password)
    return "Created new user"

# Login function
def login(username, password):
    if username in users and users[username] == hash_password(password):
        return "Login Successful"
    return "Login Failed"

# Example usage
print(register("john", "mypassword"))  
print(login("john", "mypassword"))     
print(login("john", "wrongpass"))      
