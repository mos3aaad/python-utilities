import re
from globals import again

##7. SIMPLE EMAIL VALIATOR
def emailv():
 print("Welcome to Simple email validator!")
 try:
    email = input("Enter email: \n")
    if "@" not in email or "." not in email:
        raise ValueError("Email not valid")
    parts = email.split("@")
    if len(parts) != 2 or not parts[0] or not parts[1]:
        raise ValueError("Email not valid")
    domain_parts = parts[1].split(".")
    if len(domain_parts) < 2 or not all(domain_parts):
        raise ValueError("Email not valid")
    print("Email is valid!")
 except ValueError:
     print("Email isn't valid")
 again(emailv)

##8. SIMPLE EMAIL VALIDATOR USING re           
def emailvre():
    print("Welcome to Simple email validator but this time coded with re!")
    email = input("Enter email: \n")
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        print("Email valid!")
    else:
        print("Email invalid!")
    again(emailvre)
    
##9. SIMPLE EMAIL VALIDATOR USING re           
def checker():
    users = [
    {"name": "mohamed", "pass": "123"},
    {"name": "ahmed", "pass": "456"},
    {"name": "karim", "pass": "789"}
]
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    for user in users:
        if user["name"] == name and user["pass"] == password:
            print(f"Login Successfull!\nWelcome, {name}!") 
            return
    print("Invalid name or password.")
    again(checker)            
