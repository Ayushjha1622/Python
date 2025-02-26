str = input("Enter your string: ")

reversed_str = ""


for char in str:
    reversed_str = char + reversed_str

print(reversed_str)