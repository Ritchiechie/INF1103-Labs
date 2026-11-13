from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order
from product import Product

supplier = Supplier("S001", "TechSupply", "sales@techsupply.com")
guitar = PhysicalProduct("P001", "Guitar", 500.00, 5, supplier, 3.5)
editor = DigitalProduct("P002", "Photo Editor", 49.99, 100, supplier, 250)

# PREDICT 1: after `del supplier`, can each product still show its supplier info?
del supplier
guitar.display_supplier()
editor.display_supplier()

# PREDICT 2: after removing the guitar from inventory A, does it still work?
inv_a = Inventory()
inv_b = Inventory()
inv_a.add_product(guitar)
inv_a.remove_product("P001")
guitar.display_information()
inv_b.add_product(guitar)
inv_b.add_product(editor)

# PREDICT 3: if you add the same Product to two different Orders, how many OrderLine objects and how many Product objects will exist? 
order1 = Order("O1")
order2 = Order("O2")
order1.add_order_line(guitar, 2)
order1.add_order_line(editor, 1)
order2.add_order_line(guitar, 1)
order1.display_order()
order2.display_order()

# PREDICT 4: what will get_fulfilment_info() print for each product?
def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())

for product in inv_b.get_products():
    product.update_stock(10)
    print(product.get_name(), "stock:", product.get_stock())