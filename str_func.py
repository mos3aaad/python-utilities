from globals import again

## 1: LIST THE VOWELS
def vlch():
    print("Welcome the Vowel checker!")
    l = ["a","e","i","o","u"]
    r= []
    while True:
        try:
            word = input("Please Enter a Word: ").lower()
            if not word.isalpha():
                raise ValueError
            else:
                for i in word:
                    if i in l:
                        r.append(i)
                if len(r) ==0:
                    print(f"no vowels appeared in {word}")
                else:
                    print(f"there are {len(r)} vowels")
                    print(f"the vowels {r} appeared in {word}")
                    
            break
        except ValueError:    
            word = input("Please enter proper letters:\n").lower()
            continue
    del r
    again(vlch)      

##2: LETTER LOCATOR
def ll():
    print("Welcome the Letter Locator!")
    while True:
        word = input("Enter Word:\n")
        try:
            c = input("Enter letter to locate:\n")
            if len(c)>1:
                raise ValueError
            else:
                res= []
                for j in range(len(word)):
                    if word[j] == c:
                        res.append(j+1) 
                if res:
                    print(f"the letter {c} is the {res} in {word}")
                else:
                    print(f"the letter {c} hasnt appeared in the word")
            break
        except ValueError:
            print("Please enter a single char to locate")
    del res
    again(ll)
              
##6. LIST SORTER
def lsort():
    print("Welcome to the list sorter!")
    while True:
        try:
            print("1. List Alphabetically\n2. List Numerically")
            k = int(input("(1-2) :  "))
            if k not in (1, 2):  # Fixed condition
                print("Please enter 1 or 2.")
                continue        
            l = []
            while len(l) < 5:
                n = input(f"Enter elment {len(l) + 1}: ")
                l.append(int(n) if k == 2 else n)  # Convert to int only for numerical sorting
            print("You entered:", l)
            print("Sorted (ascending):", sorted(l))
            print("Sorted (descending):", sorted(l, reverse=True))
            break
        except ValueError:
            print("Invalid entry type. Please enter a valid value.")
    again(lsort)
                


