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
    else:
        tries -= 1
        checkpin = input("PIN Incorrect! Please try again: ")

print("Have a great day!")
