from globals import again

##5. MARIO PYRAMID!
def mario():
    while True:
        try:
            height = int(input("Enter pyramid height (positive integer): "))
            if height > 0:
                break
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * i)
    while True:
        try:
            rev = input("Would you Like the Pyramid to be reversed? (y-n)\n")
            if rev == "y" or rev == "yes":
                for i in range(height, 0, -1):
                    print(" " * (height - i) + "*" * i)
                rev = "n"
                break
            elif rev == "n" or rev == "no":
                break
        except ValueError:
            print("Invaild Entry (y-n)")
    again(mario)