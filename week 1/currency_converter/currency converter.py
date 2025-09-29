
print("welcome to our offline currency converter. ")


#ask user for input.

amt=float(input("enter amout: "))

#ask user for primary currency.

first_currency=input("enter currency: ").upper().strip()
    
    #ask user for secondary currency

second_currency=input("enter secondary currrency: ").upper().strip()

#store our exchange rate in a dcitonary.

currency_exchange={
        "USD": 1.0,
        "NGN": 1500,
        # "JPY":
        "EUR": 0.93,
         "GBP": 0.83

        }
# condition if user types in an unavailable exchange rate.

if first_currency not in currency_exchange:
      print(f"{first_currency} not available") 

elif  second_currency not in currency_exchange:
     print(f"{second_currency} not available ")
      
else:

    #have a base currency to convert all other currencies to, in this case USD.

    amount_in_usd= amt/currency_exchange[first_currency]
    converted_amount= amount_in_usd*currency_exchange[second_currency]

    #print out the result
    print(converted_amount)

#did not use a reusable function on purpose, might update the code later if need be.




