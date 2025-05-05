from str_func import vlch, ll, lsort
from emails import emailv, emailvre, checker
from multiplication import mt, mtr 
from mario import mario

#main menu
def menu():
    print("Welcome!")
    print("1. Vowels checker\n2. Letter locater\n3. Multiplication Table Generator\n4. Listed Multiplication Table Generator\n5. Mario Pyramid\n6. List Sort\n7. Email Validator\n8. Email Validator (re)\n9. Simple Authenticator\n10. Quit")
    while True:
        try:
            key = int(input("Enter your choice: (0 for Options - 10 to Quit)\n"))
            if key ==0:
                    print("1. Vowels checker\n2. Letter locater\n3. Multiplication Table Generator\n4. Listed Multiplication Table Generator\n5. Mario Pyramid\n6. List Sort\n7. Email Validator\n8. Email Validator (re)\n9. Simple Authenticator\n10. Quit")
            if key ==1:
                vlch()
            elif key == 2:
                ll()
            elif key == 3:
                mt()
            elif key == 4:
                mtr()
            elif key == 5:
                mario()
            elif key == 6:
                lsort()
            elif key == 7:
                emailv()
            elif key == 8:
                emailvre()
            elif key == 9:
                checker()
            elif key == 10:
                exit()    
            else:
                raise ValueError
        except ValueError:
            print("Try again. (1-10) (0 for Options)")    
    
    
    

menu()