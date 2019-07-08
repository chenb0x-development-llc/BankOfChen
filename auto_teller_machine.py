#!/usr/local/bin/python3

pin = 5912
tries = 3

print("Welcome to the Bank of Chen")
checkpin = input("Please enter your PIN: ")

while tries > 0:
    if str(checkpin) == str(pin):
        tries = 0
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Return card and exit")
        select = input("Please make a selection: ")
        if str(select) == "1":
            print("You are about to check your balance.")
        if str(select) == "2":
            print("You are about to deposit money.")
        if str(select) == "3":
            print("You are about to withdraw money.")
        if str(select) == "4":
            print("Goodbye.")
    else:
        tries -= 1
        checkpin = input("PIN Incorrect! Please try again: ")

print("Have a great day!")
