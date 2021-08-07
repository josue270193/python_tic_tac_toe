user_input = input()
result = ""
for char in user_input:
    if char.islower():
        result += char
    elif result == "":
        result += char.lower()
    else:
        result += "_" + char.lower()
print(result)
