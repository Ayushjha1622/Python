score = int(input("Enter your score: "))

if(score >= 101):
    print("check your number")
    exit()
1
if score > 90 and score < 100:
    print("You got an A")
elif score > 80 and score < 89:
    print("You got a B")
elif score > 70 and score < 79:
    print("You got a C")
elif score > 60 and score < 69:
    print("You got a D")
else:
    print("You got an F")