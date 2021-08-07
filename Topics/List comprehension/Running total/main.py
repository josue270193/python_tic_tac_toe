user_input = input()
number_list = [int(x) for x in user_input]
result_list = [sum(number_list[:index + 1:]) for index in range(len(number_list))]
print(result_list)
