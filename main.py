running = True
while running:
    a = int(input(""))
    o = input("")
    b = int(input(""))

    if o == "+":
            print(a + b)
            running = False
    elif o == "-":
            print(a - b)
            running = False
    elif o == "x":
            print(a * b)
            running = False
    elif o == "/":
            print(a / b)
            running = False
    elif o == "%":
            print(a % b)
            running = False
    elif o == "**":
            print(a**b)
            running = False
    else:
            print("Not a valid option")
