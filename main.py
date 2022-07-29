print("calc")
running = True
while running:
    a = int(input(""))
    o = input("Opr: ")
    b = int(input(""))

    if o == "+":
            print(a + b)
    elif o == "-":
            print(a - b)
    elif o == "x":
            print(a * b)
    elif o == "/":
            print(a / b)
    elif o == "%":
            print(a % b)
    elif o == "**":
            print(a**b)
    else:
            print("Incorrect option.")
