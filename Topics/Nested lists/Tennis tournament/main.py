lines_input = int(input())
result = list()
for _ in range(lines_input):
    user_input = input()
    match = user_input.split()
    if len(match) > 1 and match[1].lower() == "win":
        result.append(match[0])

print(result)
print(len(result))
