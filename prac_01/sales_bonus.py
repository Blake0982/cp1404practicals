"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus_rate = 10
    else:
        bonus_rate = 15
    bonus = sales * (bonus_rate/100)
    print(f"You made ${sales:.2f} in sales, you get a {bonus_rate:}% bonus, giving you ${bonus:.2f} bonus")
    sales = float(input("Enter sales: $"))
print("error invalid sales")
