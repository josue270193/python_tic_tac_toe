timezone_input = int(input())
time = 10 + timezone_input

if time >= 24:
    print("Wednesday")
elif time >= 0:
    print("Tuesday")
else:
    print("Monday")
