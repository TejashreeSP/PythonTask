import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Examples
print(is_valid_email("user@domain.com"))  
print(is_valid_email("user@domain"))      
