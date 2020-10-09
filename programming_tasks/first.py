total_cost = 0

while True:
    print("Type 'quit' to stop ")

    item = input("What item do you want to buy? ")
    if item == 'quit': break
    
    price = float(input("What is the listed price? "))

    discount = input("Does your item have a discount? ")
    if discount.lower() == 'yes':
        percent_discount = int(input("What percent discount? "))
        price -= price * (percent_discount / 100)

    tax = input("Is there tax? ")
    if tax.lower() == 'yes':
        price *= 1.13
    
    print(f"The {item} will cost ${price:.2f}")
    total_cost += price

print(f"The total cost of all your items is: ${total_cost:.2f} \nThank you!")