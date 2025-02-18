class UserAuthentication:
    def __init__(self):
        self.__users = []
    
    def authenticate(self, id, password):
        user = self.find_user(id)
        if user and user.verify_password(password):
            print(user.get_name())
            print("Login successful")
            return user
        return None
    
    def add_user(self, user):
        self.__users.append(user)
    
    def find_user(self, id):
        for user in self.__users:
            if user.get_id() == id:
                return user
        return None

class InventoryManager:
    def __init__(self):
        self.__inventory = []
    
    def add_item(self, item, quantity):
        existing_item = self.find_item(item)
        if existing_item:
            existing_item['quantity'] += quantity
        else:
            self.__inventory.append({'item': item, 'quantity': quantity})
    
    def get_items(self):
        return self.__inventory
    
    def remove_item(self, item, quantity):
        existing_item = self.find_item(item)
        if existing_item and existing_item['quantity'] >= quantity:
            existing_item['quantity'] -= quantity
            if existing_item['quantity'] == 0:
                self.__inventory.remove(existing_item)
            return True
        return False
    
    def find_item(self, item):
        for inv_item in self.__inventory:
            if inv_item['item'] == item:
                return inv_item
        return None

class TransactionManager:
    def __init__(self):
        self.__balance = 0
        self.__transactions = []
    
    def process_transaction(self, amount, description):
        if amount < 0 and not self.can_withdraw(-amount):
            return False
        self.__balance += amount
        self.__transactions.append({'amount': amount, 'description': description})
        return True
    
    def can_withdraw(self, amount):
        return self.__balance >= amount
    
    def get_balance(self):
        return self.__balance

class User:
    def __init__(self, id, name, email, phone, address, password):
        self.__id = id
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__address = address
        self.__password = password
        self.__inventory = InventoryManager()
        self.__transactions = TransactionManager()
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def verify_password(self, password):
        return self.__password == password
    
    def purchase_product_from_retail(self, product, quantity, retail_shop):
        cost = product.get_price() * quantity
        if self.__transactions.process_transaction(-cost, f"Purchase {quantity} {product.get_name()} from {retail_shop.get_name()}"):
            if retail_shop.sell_product(product, quantity, cost):
                self.__inventory.add_item(product, quantity)
                return True
        return False
    
    def get_inventory(self):
        return self.__inventory
    
    def get_transactions(self):
        return self.__transactions

class RetailShop(User):
    def __init__(self, id, name, email, phone, address, password, shop_name, shop_address):
        super().__init__(id, name, email, phone, address, password)
        self.__shop_name = shop_name
        self.__shop_address = shop_address
        self.__inventory = InventoryManager()
        self.__transactions = TransactionManager()
    
    def purchase_product(self, product, quantity, manufacturer):
        cost = product.get_price() * quantity
        if self.__transactions.process_transaction(-cost, f"Purchase {quantity} {product.get_name()}"):
            if manufacturer.sell_product(product, quantity, cost):
                self.__inventory.add_item(product, quantity)
                return True
        return False
    
    def sell_product(self, product, quantity, amount):
        if self.__inventory.remove_item(product, quantity):
            self.__transactions.process_transaction(amount, f"Sold {quantity} {product.get_name()}")
            return True
        return False
    
    def info(self):
        return f"Name: {self.get_name()}, Shop Name: {self.__shop_name}, Shop Address: {self.__shop_address}, Balance: {self.__transactions.get_balance()}"
    
    def get_inventory(self):
        return self.__inventory
    
    def get_transactions(self):
        return self.__transactions

class Manufacturer(User):
    def __init__(self, id, name, email, phone, address, password, factory_name, factory_address):
        super().__init__(id, name, email, phone, address, password)
        self.__factory_name = factory_name
        self.__factory_address = factory_address
        self.__inventory = InventoryManager()
        self.__transactions = TransactionManager()
    
    def create_product(self, name, price, purity, quantity, category):
        product = Product(name, price, purity, category)
        self.__inventory.add_item(product, quantity)
        return product
    
    def sell_product(self, product, quantity, amount):
        if self.__inventory.remove_item(product, quantity):
            self.__transactions.process_transaction(amount, f"Sold {quantity} {product.get_name()}")
            return True
        return False
    
    def info(self):
        return f"Name: {self.get_name()}, Factory Name: {self.__factory_name}, Factory Address: {self.__factory_address}"
    
    def get_inventory(self):
        return self.__inventory
    
    def get_transactions(self):
        return self.__transactions

class Product:
    def __init__(self, name, price, purity, category):
        self.__name = name
        self.__price = price
        self.__purity = purity
        self.__category = category
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def get_purity(self):
        return self.__purity
    
    def get_category(self):
        return self.__category
    
    def __eq__(self, other):
        return (self.__name == other.__name and
                self.__price == other.__price and
                self.__purity == other.__purity and
                self.__category == other.__category)

class System:
    def __init__(self):
        self.__auth = UserAuthentication()
    
    def register_user(self, user):
        self.__auth.add_user(user)
    
    def login(self, id, password):
        return self.__auth.authenticate(id, password)