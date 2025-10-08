#password strength checker 

print("welcome to password strength checker.....")

password=input("enter your preffered password: ")

 #assign conditions

special_characters =("!@#$%^&*()_+-=[]{};:'\",.<>?/|\\")

if len(password) >=8 and any(char.isalpha() for char in password) and any(char.isdigit() for char in password) and any(char in special_characters for char in password):
    print("password is strong..")
elif  len(password) >=8 and any(char.isalpha() for char in password) and any(char.isdigit() for char in password) and any(char not in special_characters for char in password):
    print("moderate password")
else:
    print("password is weak")