from Project import System, User, RetailShop, Manufacturer, Product

# Initialize the system
system = System()

# Register users
system.register_user(User("1", "John Doe", "john@example.com", "1234567890", "123 Main St", "password123"))
system.register_user(RetailShop("2", "Shop Owner", "shop@example.com", "0987654321", "456 Market St", "shop123", "Shop Name", "Shop Address"))
system.register_user(Manufacturer("3", "Factory Owner", "factory@example.com", "1122334455", "789 Industrial Rd", "factory123", "Factory Name", "Factory Address"))

# Authenticate users
print("\nAuthenticating users:")
system.login("1", "password123")  # Should print user details
system.login("2", "shop123")      # Should print retail shop details
system.login("3", "factory123")   # Should print manufacturer details
print("#" * 50)

# Create a product
print("\nCreating products:")
manufacturer = system.login("3", "factory123")
manufacturer.create_product("Widget", 10.0, "99%", 100, "Gadgets")
manufacturer.create_product("Necklace", 5.0, "98.5%", 10, "Accessories")
print("#" * 50)

# Deposit money
print("\nDepositing money:")
user = system.login("1", "password123")
retail_shop = system.login("2", "shop123")
print(retail_shop.get_transactions().get_balance())
user.get_transactions().process_transaction(10000, "Initial deposit")
retail_shop.get_transactions().process_transaction(1000, "Initial deposit")
print(retail_shop.get_transactions().get_balance())
print("#" * 50)

# Purchase product B2B
print("\nPurchasing product B2B:")
retail_shop = system.login("2", "shop123")
factory = system.login("3", "factory123")
product_1 = factory.create_product("Necklace", 5.0, "98.5%", 10, "Accessories")
product_2 = factory.create_product("Widget", 10.0, "99%", 100, "Gadgets")
print("Product details:")
print(product_1.get_name(), product_1.get_purity())
print(product_2.get_name(), product_2.get_purity())
print("Factory details:")
print(factory.info())
retail_shop.purchase_product(product_1, 5, factory)
retail_shop.purchase_product(product_2, 10, factory)
print("Retail Inventory:")
for item in retail_shop.get_inventory().get_items():
    print(f"Product: {item['item'].get_name()}, Quantity: {item['quantity']}")
print("Factory Inventory:")
for item in factory.get_inventory().get_items():
    print(f"Product: {item['item'].get_name()}, Quantity: {item['quantity']}")
print("#" * 50)

# Purchase product B2P
print("\nPurchasing product B2P:")
user = system.login("1", "password123")
retail_shop = system.login("2", "shop123")
product = retail_shop.get_inventory().find_item(product_2)
if product:
    user.purchase_product_from_retail(product['item'], 2, retail_shop)
print("User Inventory:")
for item in user.get_inventory().get_items():
    print(f"Product: {item['item'].get_name()}, Quantity: {item['quantity']}")
print("Retail Shop Inventory:")
for item in retail_shop.get_inventory().get_items():
    print(f"Product: {item['item'].get_name()}, Quantity: {item['quantity']}")
print("#" * 50)