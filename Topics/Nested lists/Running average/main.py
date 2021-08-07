user_input = input()
number_list = [int(x) for x in user_input]
average_list = [(number_list[index] + number_list[index + 1]) / 2 for index in range(len(number_list) - 1)]
print(average_list)
