from products import Products
from customer import Customer
from order import Order

headphones = Products('Headphones', 10)
phone = Products('Phone', 100)
laptop = Products('Laptop', 300)
cable = Products('Cable', 5)
connector = Products('Connector', 1)

customer_1 = Customer('Andrew', 'Garfield', '380962431562')
customer_2 = Customer('Steve', 'Jonson', '38096345454')
customer_3 = Customer('Karol', 'Gerbel', '38096341254')

order_1 = Order(customer_1)
order_1.add_product(headphones, 1)
order_1.add_product(cable, 2)
order_1.add_product(connector, 2)

order_2 = Order(customer_2)
order_2.add_product(laptop, 1)

order_3 = Order(customer_3)
order_3.add_product(phone, 1)

print(order_1)
print(order_2)
print(order_3)