import re


def is_email_correct(email_address):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email_address):
        return email_address
    else:
        is_email_correct(input("The email address you entered is incorrect\n"
                               "please re-enter your email address"))


def is_correct_phone_num(phone_number):
    a = phone_number
    while not re.match(r"^[-+]?[0-9]+$", a):
        a = input("The phone number you entered is incorrect\n please re-enter your phone number")
    return a