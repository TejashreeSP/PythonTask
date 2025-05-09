# Initial user list
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

# Create
def add_user(user):
    users.append(user)
    print(f"User added: {user}")

# Read
def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

# Update
def update_user(user_id, name=None, email=None):
    for user in users:
        if user["id"] == user_id:
            if name:
                user["name"] = name
            if email:
                user["email"] = email
            print(f"User updated: {user}")
            return
    print("User not found.")

# Delete
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    print(f"User with ID {user_id} deleted.")

# Example 
add_user({"id": 3, "name": "Charlie", "email": "charlie@example.com"})
print(get_user_by_id(2))
update_user(1, name="Alicia")
delete_user(2)
print(users)
