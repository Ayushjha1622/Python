num = int(input("enter your number: "))

for i in range (1,11):
    if i == 5:
        continue
    print(f"{num} X {i} = {num*i}")
    
    