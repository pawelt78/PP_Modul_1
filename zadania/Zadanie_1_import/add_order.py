from zadania.Zadanie_1_import.shop_products import find_product_by_name

def add_new_order(name, order_quantity):
    product = find_product_by_name(name)
    order = []
    order.append({
        "name": name,
        "quantity": order_quantity,
        "value": (order_quantity * product["product_details"]["price"])
    })
    subtraction(name, order_quantity)
    return order


def subtraction(name, order_quantity):
    product = find_product_by_name(name)
    product["product_details"]["quantity"] -= order_quantity




