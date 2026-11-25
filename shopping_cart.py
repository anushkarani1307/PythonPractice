cart = {'P1': 2, 'P2': 1, 'P3': 5}

cart['P5'] = 1
cart['P2'] = cart['P2'] + 3
removed = cart.pop('P3')

print("cart after steps 1-3:", cart)
print("quantity removed in step 3:", removed)
print("quantity of P9:", cart.get('P9', 0))
print("sorted product ids:", sorted(cart.keys()))
print("different products:", len(cart))
print("total units:", sum(cart.values()))
high = max(cart, key=cart.get)
print("product with highest quantity:", high)