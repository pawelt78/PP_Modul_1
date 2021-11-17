from zadania.Zadanie_1_import.add_order import add_new_order
from zadania.Zadanie_1_import.shop_products import is_product_in_schop

print("Witaj w naszym sklepie!")
print("")

order_name = input("Podaj jaki produkt chcesz zamówić w naszym sklepie: ")
order_quantity = int(input("Podaj jaka ilość wybranego produktu Cię interesuje? "))

if not is_product_in_schop(order_name, order_quantity):
    print(f"Niestety {order_name} nie ma na stanie lub zamówienie jest za duże...")
else:
    print("Zamówienie: ")
    print(f"{add_new_order(order_name, order_quantity)}")


