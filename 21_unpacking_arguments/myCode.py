fruitPrice = {"Manzana": 5000, "Naranja": 2000, "Pera": 4000}


def total(**args):
    sum = 0
    for fruit, price in fruitPrice.items():
        sum += price

    return sum


print(f"The total price will be: {total(**fruitPrice)}")


print("##################################################")

# acepting and printing an arbitrary number of arguments without explicitly specifying them in the function's parameter list


def showElemnts(*args):
    for arg in args:
        print(arg)


showElemnts([2, 3, 4, 5, "Hola", "Enero"])
