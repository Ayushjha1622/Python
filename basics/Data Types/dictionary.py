chai_types = {"masala":"spicy","ginger":"zesty","green": "mild"}
# print(chai_types)

# print(chai_types.get("ginger"))


# chai_types["green"] = "fresh"
# print(chai_types)


# for chai in chai_types:
#     print(chai, chai_types[chai])


# for key, value in chai_types.items():
#     print(key, value)


# if "masala" in chai_types:
#     print(" i have tea")



# chai_types["earl grey"] = "citrus"
# print(chai_types)


# chai_types.pop("ginger")

# print(chai_types)
# del chai_types["green"]
# print(chai_types)


# chai_types_copy = chai_types.copy()



# tea_shop = {
#     "chai": {"masala":"spicy","ginger":"zesty"},
#     "tea":{"green":"mild","black":"strong"}
# }

# # print(tea_shop)
# print(tea_shop["chai"]["ginger"])



squared_num = {x:x**2 for x in range(6)}
# print(squared_num)

# squared_num.clear()


keys = ["a","b","c"]
default_value = "alphabets"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)

