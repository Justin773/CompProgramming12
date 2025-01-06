import os
import random as r
amt = int(r.randint(1000,9999))

def main():
    def success():
        global amt
        print(f"Welcome.\nYour balance is ${amt}")
        exit()
    def setpin():
        while True:
            pin = input("Please set a pin.\n")
            if not pin.isdigit():
                print("Only numbers.")
                continue
            if len(pin) != 4:
                print("You inputed more or less than 4 digits.")
            else:
                print(f"Your pin is {pin}.")
                os.system('clear')
                break
        x = 0
        y = 3
        while True:
            while x < 3:
                test = input("Please input your pin:\n")
                if test == pin:
                    success()
                else:
                    y -= 1
                    print(f"You inputted the wrong pin.\nYou have {y} attempts left.")
                    x += 1
            if x == 3:
                print("Too many incorrect attempts.")
                return
    setpin() 
main()