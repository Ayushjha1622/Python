while True: 
    num = int(input("Enter num: "))
    
    if 1 <= num <= 10:
        print("You entered a valid number")
        break
    else:
        print("Invalid number, please enter a number between 1 and 10")