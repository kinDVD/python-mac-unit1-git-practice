print("Welcome to GC Fruit Market!")
name = input("What is your name? ")

fruit = ["apple", "bunches of grapes", "orange"]
price = ["2", "1", "3"]
apple_list = []
grape_list = []
orange_list = []
choose_prompt = "Which fruit would you like to buy?"

while True:
    print(f"Welcome {name}. {choose_prompt}")
    print(f"1) {fruit[0]} ${price[0]}")
    print(f"2) {fruit[1]} ${price[1]}")
    print(f"3) {fruit[2]} ${price[2]}")
    buy = input(">")
    cart = int(buy) - 1
    if cart == 0:
        apple_list.append(cart)
    elif cart == 1:
        grape_list.append(cart)
    elif cart == 2:
        orange_list.append(cart)
    fruit_selection = fruit[cart]
    cost = price[cart]
    print(f"You bought 1 {fruit_selection} at ${cost} a piece.")
    repeat = input(f"Would you like to buy another piece of fruit? y/n ")

    if repeat == "y":
        loop = True

    if repeat == "n":
        a = len(apple_list)
        g = len(grape_list)
        o = len(orange_list)
        pa = a * 2
        pg = g * 1
        po = o * 3
        print(f"Order for {name}")
        print(f"{a} apple(s) at ${pa} a piece")
        print(f"{g} bunches of grapes at ${pg} a piece")
        print(f"{o} orange(s) at ${po} a piece")
        sub = pa + pg + po
        print(f"Sub Total: ${sub}")
        tax = sub * .05
        print(f"5% Tax: {tax}")
        total = sub + tax
        print(f"Total: ${total}")
        break