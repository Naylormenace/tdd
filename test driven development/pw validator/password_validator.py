def is_password_secure(password):
    return min_lent(password) and uppercase(password) and lowercase(password)  and number(password) and special(password)

def min_lent(password):
    for char in password:
        if len(password) < 8:
            return False
        else:
            return True
        
def uppercase(password):
    for char in password:
        if char.isupper():
            return True
    
    return False

def lowercase(password):
    for char in password:
        if char.islower():
            return True

    return False
    
def number(password):
    for char in password:
        if char.isnumeric():
            return True

    return False

def special(password):
    for char in password:
        if (char.isalnum() == False) and (char != " "):
            return True
    
    return False