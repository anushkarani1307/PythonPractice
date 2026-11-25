name = ' wireless MOUSE '
sku = ' sku-0017 '
price = ' 1,299.50 '
qty = ' 3 '
gst_rate = 18

name = name.strip().title()
sku = sku.strip().upper()
price = float(price.strip().replace(',', ''))
qty = int(qty.strip())

subtotal = price * qty
gst = subtotal * gst_rate / 100
total = subtotal + gst

print("name:", name)
print("sku:", sku)
print("price:", price)
print("qty:", qty)
print("subtotal:", subtotal)
print("gst:", round(gst, 2))
print("total:", round(total, 2))
print("\nPrinted Invoice:")
print(f"{name} | {sku} | {qty} x {price:,.2f} = {subtotal:,.2f} | GST {gst:.2f} | Total {total:,.2f}")