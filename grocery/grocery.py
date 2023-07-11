products = []

while True:
    try:
        item = input().strip().lower()
    except EOFError:
        for product in sorted(products, key=lambda s: s["name"]):
            print("{qty} {item}".format(item = product["name"].upper(), qty = product["qty"]))
        break
    else:
        if bool(products) == False:
            products.append({"name": item, "qty": 1})
        else:
            for product in products:
                if product["name"] == item:
                    product["qty"]+=1
                    break
                if product == products[-1]:
                    products.append({"name": item, "qty": 1})
                    break
