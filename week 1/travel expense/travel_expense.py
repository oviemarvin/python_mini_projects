

#create a list to store the input data

list_of_people=[]

num_of_people= int(input("enter number of people: "))

total_spent=float(input("enter total amount spent in $: "))

for i in range(num_of_people):
    #collect details of persons, how much they spent and what they paid for 

    name_of_person=str(input("enter name of person: "))
    expense=float(input(f"how much did {name_of_person} spend: "))
    purpose=str(input(f"what did {name_of_person} pay for: "))

    #store input in the dictionary
    list_of_people.append({"name": name_of_person, "expense": expense, "purpose": purpose})
print(list_of_people)

#calculate share
share= total_spent/num_of_people
print(f"total trip expense: ${total_spent}")
print(f"each person\'s share: ${share}")

#claculate the balance owed if at all
for person in list_of_people:
    balance=person["expense"] - share
    if balance > 0:
        print(f"{person["name"]} should recieve ${balance}")
    elif balance < 0:
        print(f"{person["name"]} owes ${- balance}")
    else:
        print(f"{person["name"]} is good to go")

