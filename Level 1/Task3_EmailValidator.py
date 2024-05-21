import re


def is_valid_email(email):

    # Define the regex pattern for a valid email address
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Match the email string against the regex pattern
    if re.match(email_regex, email):
        return True
    else:
        return False


test_email = input('Enter emails: ')
flag = is_valid_email(test_email)

if flag == True:
    print(f'{test_email} is a valid Email Address')
else:
    print(f'{test_email} is not a valid Email Address')
