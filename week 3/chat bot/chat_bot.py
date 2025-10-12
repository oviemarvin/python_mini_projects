
#offline chatbot


#function to get user input.

def get_input():
    user_input=input("Hi i am Frosti, Type \"bye\" to exit. ").lower().strip()
    return user_input


#function to carry out responses based off user input.

def get_response(user_input):


        if user_input=="hey" or user_input=="hi" or user_input=="hello":
            return("Hello, how are you")
        elif user_input=="how are you":
            return("i am doing great, thank you..")
        elif user_input=="i am fine":
            return("Good to hear")
        elif user_input=="":
            return("say something...")
        elif user_input=="bye":
            exit()
        elif user_input=="what are you up to":
             return("nothing much, just chilling.")
        elif user_input=="cool":
             return("yeah great! ")
        elif user_input=="okay":
             return("yeahh!..")
        elif user_input=="tell me about yourself":
             return("I am an offline based chatbot, programmed by Marvin, designed to give tailored replies to specific questions...")
        else:
            return("Did not quite catch that...")
        

#function to carry out repeated process of getting input from the user

def chat_process():
     while True:
            process=get_input()
            if process=="bye":
                 break
            else:
                 process=get_response(process)
                 print(f"{process}")
    


chat_process()









