number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    product = number * i # type: ignore
    print(f"{number} * {i} = {product}") # type: ignore