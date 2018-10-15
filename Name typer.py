namn = "Sofia"
x_range = len(namn)
range_stuff = 0
for ppp in range (10):
    for x in range(x_range):
        range_stuff += 1
        print(str(namn)[:range_stuff])
    for y in range(x_range):
        range_stuff -= 1
        print(str(namn)[:range_stuff])
    print("\n")
