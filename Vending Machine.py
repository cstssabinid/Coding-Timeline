def vending_machine():
    price = 50
    total_amount = 0
    print("Welcom to the coca_cola vending machine!")
    print("The price for a cane is 50cents")
    print("Please insert coins of 5cents, 10cents, 25cents.")

    while total_amount < price:
        amount_due = price - total_amount
        print("Amount due =",amount_due)
        coin = int(input("Please insert coin of (5,10,25)cents:"))
        if coin not in (5,10,25):
            print("Invalid coin, please insert the requested coin.")
            continue
        total_amount += coin
    balance = total_amount - price
    if balance == 0:
        print("Thank you, enjoy your coca_cola!")
    else:     
        print("Thank you, enjoy your coca_cola!, your balance due is:",balance)
vending_machine()