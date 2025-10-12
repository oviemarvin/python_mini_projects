import random
print("welcome to my guessing game ")
correct_num = random.randint(1, 70)
counter=0
while True:
    try:    
        guessed_number = int(input("Take a guess: "))
    except:
        print("invalid Input..")
        continue
    counter +=1
    if guessed_number < 1 or guessed_number > 70:
        print("Your maximum guess range is between 1 and 70 ")
        continue
    elif guessed_number < correct_num:
        print(f"{guessed_number} is lower than Answer ")
    elif guessed_number>correct_num:
        print(f"{guessed_number} is higher than Answer ")
    else:
        guessed_number== correct_num
        print(f"Hell Yeah ... Impressive!!!!  You guessed it in {counter} attempts")
        break
   
        
    

        
    



