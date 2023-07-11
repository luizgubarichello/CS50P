due_amount = 50
while due_amount > 0:
    print(f"Amount Due: {due_amount}")
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        due_amount -= coin
print(f"Change Owed: {-due_amount}")
