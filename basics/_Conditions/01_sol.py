age = int(input("provide me age: "))


if(age < 13):
    print("you are a child")
elif(age > 13 and age <19):
    print("you are Teanager")
elif(age < 60):
    print("Adult")
else:
    print("senior")