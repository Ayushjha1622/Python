str = "elephant"


for char in str:
    if str.count(char) == 1:
        print(f"The character '{char}' appears only once in the string.")
        break