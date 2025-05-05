## 0. PLAY AGAIN
def again(option):
    while True:
        again= input("\nWould you like to try again? (yes/no) (y/n) \n").lower()
        if again == "yes" or again == "y":
            option()
            break
        elif again == "no" or again == "n":
            break 
        else:
            print("Invalid response  (yes/no) (y/n)")
