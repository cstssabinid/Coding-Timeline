
def computepay(hours,rate):
    if hours <= 40:
        totalpay = hours * rate
    else:
        normalpay = 40 * rate 
        extrahour = (hours - 40) 
        extrapay = extrahour * (rate * 1.5)
        totalpay = normalpay + extrapay
    return totalpay
hours= float(input("Enter hours of working:"))
rate= float(input("Enter pay_rate per hour"))

pay = computepay(hours,rate)
print("Normal Pay is:",pay)
