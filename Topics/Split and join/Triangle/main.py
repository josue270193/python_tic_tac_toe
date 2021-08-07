count = int(input())
block = "#"
max_len = (count * 2) - 1

for index in range(count):
    new_row = block + (block * 2 * index)
    new_row = new_row.center(max_len)
    print(new_row)
