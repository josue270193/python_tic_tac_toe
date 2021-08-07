n_army = int(input())

if n_army < 1:
    print("no army")
elif 1 <= n_army <= 9:
    print("few")
elif 10 <= n_army <= 49:
    print("pack")
elif 50 <= n_army <= 499:
    print("horde")
elif 500 <= n_army <= 999:
    print("swarm")
else:
    print("legion")
