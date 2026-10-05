shopping_list = [
    {"item": "Notebook", "price": 150, "purchased": True},
    {"item": "Pen", "price": 30, "purchased": True},
    {"item": "USB Drive", "price": 900, "purchased": False},
]

to_buy = [entry["item"] for entry in shopping_list if not entry["purchased"]]
remaining = sum([entry["price"] for entry in shopping_list if not entry["purchased"]])

print("Still need to buy:", to_buy)
print("Remaining cost:", remaining)