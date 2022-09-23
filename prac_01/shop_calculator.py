number_of_item = int(input("Number of items: "))
n = number_of_item - 1
if n < 0:
    print("error invalid number of items")
else:
    total_price = float(input("Price of item: "))
    for i in range(0, n, 1):
        total_price = total_price + float(input("Price of item: "))
    if total_price > 100:
        total_price = total_price * 0.9
    print(f"Total price for {number_of_item} items is ${total_price:.2f}")
