import random

chars = "abcdefghijklmnopqfstuvwyxz"
numbers = "123456789"
symbols = "#-_.!"

while 1:
    password_len = int(input("What length would you like your password to be : "))
    password_count = int(input("How many passwords would you like : "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_total = random.choice(chars + numbers +symbols)
            password      = password + password_total
        print("Here is your password : " + password)
