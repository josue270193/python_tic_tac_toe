user_money = int(input())

count_sheep = user_money // 6769
count_cow = user_money // 3848
count_pig = user_money // 1296
count_goat = user_money // 678
count_chicken = user_money // 23

if count_sheep > 0:
    print("{} sheep".format(count_sheep))
elif count_cow > 0:
    count_string = "s" if count_cow > 1 else ""
    print("{} cow{}".format(count_cow, count_string))
elif count_pig > 0:
    count_string = "s" if count_pig > 1 else ""
    print("{} pig{}".format(count_pig, count_string))
elif count_goat > 0:
    count_string = "s" if count_goat > 1 else ""
    print("{} goat{}".format(count_goat, count_string))
elif count_chicken > 0:
    count_string = "s" if count_chicken > 1 else ""
    print("{} chicken{}".format(count_chicken, count_string))
else:
    print("None")
