age = int(input("Enter your age: "))
day = "wednesday"


price = 12 if age >= 18 else 8

if day == "wednesday":
    price = price - 2
    
print(f"Ticket Price for u: {price}$")