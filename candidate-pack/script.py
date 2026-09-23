import json

files = ["responses/orders_page1.json", "responses/orders_page2.json"]

all_orders = []
for filename in files:
    with open(filename) as f:
        data = json.load(f)
    all_orders.extend(data["data"])

for order in all_orders:
    order_id = order["id"]
    subtotal = order["subtotal"]
    tax = order["tax"]
    shipping = order["shipping"]
    total = order["total"]

    computed = subtotal + tax + shipping
    diff = computed - total

    if diff != 0:
        print(f"{order_id}: Computed(subtotal + tax + shipping)={computed}, total field={total}, difference={diff}")
    else:
        print(f"{order_id}: OK (total={total})")