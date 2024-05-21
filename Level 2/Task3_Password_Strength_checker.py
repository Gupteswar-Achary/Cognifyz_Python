import string


# FUnction to check the strength
def password_strength_checker(password):
    # Function to check presence of uppercase
    def uppercase(isupper):
        return any(char.isupper() for char in isupper)

    # Function to check presence of lowercase
    def lowercase(islower):
        return any(char.islower() for char in islower)

    # Function to check presence of digits
    def digits(isdigit):
        return any(char.isdigit() for char in isdigit)

    # Function to check presence of special characters
    def symbols(issymbol):
        special_chars = string.punctuation
        for char in issymbol:
            if char in special_chars:
                return True
    # Conditions for the strength of password
    '''
    Strong password must contain 12 characters including uppercase, lowercase, digits and symbols.
    If miss only one of these(uppercase, lowercase, digits, symbols) it will be considered as average.
    If miss more than one character, it will be considered as too weak.
    '''
    if len(password) < 12:
        print("Password is too weak. Password must be at least 12 characters long.")
    elif uppercase(password) and lowercase(password) and digits(password) and symbols(password):
        print("Password is strong")
    elif uppercase(password) and lowercase(password) and digits(password):
        print("Password is average.\nAdd Special Characters")
    elif uppercase(password) and lowercase(password) and symbols(password):
        print("Password is average.\nAdd digits")
    elif uppercase(password) and digits(password) and symbols(password):
        print("Password is average.\nAdd lower case")
    elif lowercase(password) and digits(password) and symbols(password):
        print("Password is average.\nAdd uppercase")
    else:
        print("Password is too weak. Use uppercase, lowercase, digits and symbols.")


# Main function
def main():
    password = input("Enter your password: ")
    password_strength_checker(password)


if __name__ == '__main__':
    main()
