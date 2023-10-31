fruitPrice = {"Manzana": 5000, "Naranja": 2000, "Pera": 4000}


def total(**args):
    sum = 0
    for fruit, price in fruitPrice.items():
        sum += price

    return sum


print(f"The total price will be: {total(**fruitPrice)}")
