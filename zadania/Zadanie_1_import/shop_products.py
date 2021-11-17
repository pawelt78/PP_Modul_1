products = [
    {
        "name": "herbata",
        "product_details":
            {
                "quantity": 5,
                "price": 3.55
            },
    },
    {
        "name": "kawa",
        "product_details":
            {
                "quantity": 10,
                "price": 8.05
            },
    },
    {
        "name": "chleb",
        "product_details":
            {
                "quantity": 15,
                "price": 2.60
            },
    },
]

def find_product_by_name(name):
    for product in products:
        if product["name"] == name:
            return product

def is_product_in_schop(name, order_quantity):
    if not find_product_by_name(name) or order_quantity > find_product_by_name(name)["product_details"]["quantity"]:
        return False
    return True