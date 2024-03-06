import re


def pw_checker(password):
    if len(password) > 12:
        return 'password is to long'
    if re.search('[åäöÅÄÖ]', password):
        return "password can't contain å, ä, ö."
    if not any(char.isdigit() for char in password):
        return "Password must contain least 1 num"
    return "password is ok."


pw = input('chose a new password:')
result = pw_checker(pw)
print(result)
