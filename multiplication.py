from globals import again

##3: MULTIPLICATION TABLE
def mt():
    print("Welcome the Multiplication Table Generator!")
    while True:
        try:
            num = int(input("Enter a Number:\n"))
            for i in range(1, num+1):
                print(f"{num} x {i} = {num * i}")
            break
        except ValueError:
            print("Please enter a number (integer)")
    again(mt)

##4. MULTIPLICATION TABLE LISTED
def mtr():
    print("Welcome to the Listed Multiplication Table Generator!")
    while True:
        try:
            num = int(input("Enter a number to stop at: "))
            final = []
            for i in range(1, num + 1):
                l = []
                for j in range(1, i + 1):
                    l.append(i * j)
                final.append(l) 
            del l
            print(final)
            break
        except ValueError:
            print("Only Numbers are allowed!\n")  
    again(mtr) 