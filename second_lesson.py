while True: 
    price = int(input("What is the price of your purchase (in dollars)? "))
    print("You can save: ", end='')
    if price > 100:
        savings = 40
    elif price >= 75:
        savings = 30
    elif price >= 50:
        savings = 25
    elif price >= 25:
        savings = 10
    elif price < 25:
        savings = 0
    else:
        print("Please enter a valid number next time. ")
        continue

    price -= price * (savings / 100)
    print(f"You can save {savings}% and the final cost is ${int(price)}")

    repeat = input("Would you like to enter the cost of another purchase? ")
    if repeat.lower() == 'yes':
        continue 
    
    else:
        break