user_input = input()
number_list = [int(x) for x in user_input]
odd_list = [x for x in number_list if x % 2 == 1]
print(odd_list)
