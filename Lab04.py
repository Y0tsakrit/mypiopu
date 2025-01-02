class Bank():
    def __init__(self,name):
        self.__name = name
        self.__users = []
        self.__atms = []
        self.__sellers = []
    

    def get_user(self):
        return self.__users
    def get_atm(self):
        return self.__atms
    def add_user(self, user):
        self.__users.append(user)
    def add_atm_machine(self, atm):
        self.__atms.append(atm)
    def add_seller(self, seller):
        self.__sellers.append(seller)

    
    def search_user_from_id(self, user_id):
        for user in self.__users:
            if user.get_user_id() == user_id:
                return user
        return None
    
    def search_account_from_card(self, card_num):
        for user in self.__users:
            for account in user.get_user_acc():
                if account.get_acc_card().get_card_num() == card_num:
                    return account
        return None
    
    def search_atm_machine(self, atm_id):
        for atm in self.__atms:
            if atm.atm_no == atm_id:
                return atm
        return None
    
    def search_account_from_account_no(self, acc_no):
        for user in self.__users:
            for account in user.get_user_acc():
                if account.get_acc_id() == acc_no:
                    return account
        return None
    def search_seller(self, name):
        for seller in self.__sellers:
            if seller.get_seller_name() == name:
                return seller
        return None

class User():
    def __init__(self, user_id, user_name):
        self.__user_id = user_id
        self.__user_name = user_name
        self.__user_acc = []

    def search_account(self, acc_id):
        for account in self.__user_acc:
            if account.get_acc_id() == acc_id:
                return account
        return None

    def get_user_id(self):
        return self.__user_id
    def get_user_name(self):
        return self.__user_name
    def get_user_acc(self):
        return self.__user_acc
    def add_account(self, acc):
        self.__user_acc.append(acc)



#Class
class Account():
    def __init__(self, acc_id, acc_name, balance):
        self.__acc_id = acc_id
        self.__acc_name = acc_name
        self.__acc_card = None
        self.__acc_balance = balance
        self.__acc_transaction = []

    
    def get_acc_id(self):
        return self.__acc_id
    def get_acc_name(self):
        return self.__acc_name
    def get_acc_card(self):
        return self.__acc_card
    def get_acc_balance(self):
        return self.__acc_balance
    def set_acc_balance(self, balance):
        self.__acc_balance += balance
    def get_acc_transaction(self):
        return self.__acc_transaction
    def set_acc_transaction(self, transaction):
        self.__acc_transaction.append(transaction)
    def get_card(self):
        return self.__acc_card
    def add_card(self, card):
        self.__acc_card = card

#Subclass
class SavingAccount(Account):
    rate = 0.5
    def __init__(self, acc_id, acc_name, balance):
        super().__init__(acc_id, acc_name, balance)

class FixDepositAccount(Account):
    rate = 2.5
    def __init__(self, acc_id, acc_name, balance):
        super().__init__(acc_id, acc_name, balance)




#Class
class Card():
    def __init__(self,num, acc,pin):
        self.__card_num = num
        self.__card_acc_num = acc
        self.__card_pin = pin
    
    def get_card_num(self):
        return self.__card_num
    def get_card_acc(self):
        return self.__card_acc_num
    def get_card_pin(self):
        return self.__card_pin

#Subclass
class Debitcard(Card):
    def __init__(self, num, acc, pin):
        super().__init__(num, acc,pin)
        fee = 300


class Atmcard(Card):
    def __init__(self, num, acc, pin):
        super().__init__(num, acc,pin)
        fee = 150



class Atmmachine():

    withdraw_limit = 20000

    def __init__(self, atm_id, atm_amount):
        self.__atm_id = atm_id
        self.__atm_amount = atm_amount

    @property
    def atm_no(self):
        return self.__atm_id

    def insert_card(self, card, pin):
        if card.get_card_pin() == pin:
            return("Card inserted successfully")
        return None

    def deposit(self, account, amount):
        if amount > 0:
            account.set_acc_balance(amount)
            account.set_acc_transaction(f"D : {amount}-{account.get_acc_balance()}")
            self.__atm_amount += amount
            return True
        return ("Error")

    def withdraw(self, account, amount):
        if amount > 0 and amount <= self.withdraw_limit:
            account.set_acc_balance(-amount)
            account.set_acc_transaction(f"W : {amount}-{account.get_acc_balance()}")
            self.__atm_amount -= amount
            return True
        return ("Error")

    def transfer(self,account, amount, target_account):
        if amount > 0 and amount <= 100_000:
            account.set_acc_balance(-amount)
            account.set_acc_transaction(f"Paid : {amount}-{account.get_acc_balance()} to {target_account.get_acc_id()}")
            target_account.set_acc_balance(amount)
            target_account.set_acc_transaction(f"Receive : {amount}-{target_account.get_acc_balance()} from {account.get_acc_id()}")
            return True


class Seller:
    def __init__(self,seller_no,name):
        self.__seller_no = seller_no
        self.__name = name
        self.__edc_list = []
    
    def add_edc(self,edc):
        self.__edc_list.append(edc)

    def get_seller_name(self):
        return self.__name
    
    def search_edc_from_no(self, edc_no):
        for edc in self.__edc_list:
            if edc.get_edc_no() == edc_no:
                return edc
        return None
    
    def paid(self, acc, amount, seller_account):
        if amount > 0:
            acc.set_acc_balance(-amount)
            acc.set_acc_transaction(f"EP : {amount}-{acc.get_acc_balance()} to {seller_account.get_acc_id()}")
            seller_account.set_acc_balance(amount)
            seller_account.set_acc_transaction(f"EP : {amount}-{seller_account.get_acc_balance()} from {acc.get_acc_id()}")
            return True
        return False

class EDC_machine:
    def __init__(self,edc_no,seller):
        self.__edc_no = edc_no
        self.__seller = seller
    
    def get_edc_no(self):
        return self.__edc_no
    
    def paid(self, card, amount, seller_account):
        if amount > 0:
            card.get_card_acc().set_acc_balance(-amount)
            card.get_card_acc().set_acc_transaction(f"P : {amount}-{card.get_card_acc().get_acc_balance()} to {seller_account.get_acc_id()}")
            seller_account.set_acc_balance(amount)
            seller_account.set_acc_transaction(f"P : {amount}-{seller_account.get_acc_balance()} from {card.get_card_acc().get_acc_id()}")
            return True
        return False

scb = Bank('SCB')
scb.add_user(User('1-1101-12345-12-0','Harry Potter'))
scb.add_user(User('1-1101-12345-13-0','Hermione Jean Granger'))
scb.add_user(User('9-0000-00000-01-0','KFC'))
scb.add_user(User('9-0000-00000-02-0','Tops'))
harry = scb.search_user_from_id('1-1101-12345-12-0')
harry.add_account(SavingAccount('1234567890', harry, 20000))
harry_account = harry.search_account('1234567890')
harry_account.add_card(Atmcard('12345', harry, '1234'))
hermione = scb.search_user_from_id('1-1101-12345-12-0')
hermione.add_account(SavingAccount('0987654321',hermione,2000))
hermione_account1 = hermione.search_account('0987654321')
hermione_account1.add_card(Debitcard('12346',hermione_account1,'1234'))
hermione.add_account(FixDepositAccount('0987654322',hermione,1000))
kfc = scb.search_user_from_id('9-0000-00000-01-0')
kfc.add_account(SavingAccount('0000000321', kfc, 0))
tops = scb.search_user_from_id('9-0000-00000-02-0')
tops.add_account(SavingAccount('0000000322', tops, 0))

scb.add_atm_machine(Atmmachine('1001',1000000))
scb.add_atm_machine(Atmmachine('1002',200000))

temp = Seller('210','KFC')
temp.add_edc(EDC_machine('2101',temp))
scb.add_seller(temp)
temp = Seller('220',"Tops")
temp.add_edc(EDC_machine('2201',temp))
scb.add_seller(temp)

# for i in scb.get_user():
#     print(i.get_user_name())
#     for j in i.get_user_acc():
#         print(f"id: {j.get_acc_id()}")
#         print(f"balance : {j.get_acc_balance()}")
#         if j.get_acc_card() != None:
#             print(f"card : {j.get_acc_card().get_card_num()}")
#         print(f"transaction : {j.get_acc_transaction()}")
#         print("")



#################################################
# Test Case #1
# Harry's ATM No :  12345
# Harry's Account No :  1234567890
# Success
# Harry account before deposit :  20000
# Deposit 1000
# Harry account after deposit :  21000

atm_machine = scb.search_atm_machine('1001')
harry_account = scb.search_account_from_card('12345')
atm_card = harry_account.get_card()
print("Test Case #1")
print("Harry's ATM No : ",atm_card.get_card_num())
print("Harry's Account No : ",harry_account.get_acc_id())
print(atm_machine.insert_card(atm_card, "1234"))
print("Harry account before deposit : ",harry_account.get_acc_balance())
print("Deposit 1000")
atm_machine.deposit(harry_account,1000)
print("Harry account after deposit : ",harry_account.get_acc_balance())
print("")



#################################################
# Test Case #2
# Hermione's ATM No :  12346
# Hermione's Account No :  0987654321
# Success
# Hermione account before withdraw :  2000
# withdraw 1000
# Hermione account after withdraw :  1000

atm_machine = scb.search_atm_machine('1002')
hermione_account = scb.search_account_from_card('12346')
atm_card = hermione_account.get_card()
print("Test Case #1")
print("Hermione's ATM No : ",atm_card.get_card_num())
print("Hermione's Account No : ",hermione_account.get_acc_id())
print(atm_machine.insert_card(atm_card, "1234"))
print("Hermione account before deposit : ",hermione_account.get_acc_balance())
print("Deposit 1000")
atm_machine.withdraw(hermione_account,1000)
print("Hermione account after deposit : ",hermione_account.get_acc_balance())
print("")




#################################################
# Test Case #3
# Harry's Account No :  1234567890
# Hermione's Account No :  0987654321
# Harry account before transfer :  21000
# Hermione account before transfer :  1000
# Harry account after transfer :  11000
# Hermione account after transfer :  11000

atm_machine = scb.search_atm_machine('1001')
harry_account = scb.search_account_from_card('12345')
hermione_account = scb.search_account_from_card('12346')
print("Test Case #3")
print("Harry's Account No : ",harry_account.get_acc_id())
print("Hermione's Account No : ", hermione_account.get_acc_id())
print("Harry account before transfer : ",harry_account.get_acc_balance())
print("Hermione account before transfer : ",hermione_account.get_acc_balance())
atm_machine.transfer(harry_account, 10000, hermione_account)
print("Harry account after transfer : ",harry_account.get_acc_balance())
print("Hermione account after transfer : ",hermione_account.get_acc_balance())
print("")

#################################################
# Test Case #4
# Hermione's Debit Card No :  12346
# Hermione's Account No :  0987654321
# Seller :  KFC
# KFC's Account No :  0000000321
# KFC account before paid :  0
# Hermione account before paid :  11000
# KFC account after paid :  500
# Hermione account after paid :  10500

hermione_account = scb.search_account_from_account_no('0987654321')
debit_card = hermione_account.get_card()
kfc_account = scb.search_account_from_account_no('0000000321')
kfc = scb.search_seller('KFC')
edc = kfc.search_edc_from_no('2101')

print("Test Case #4")
print("Hermione's Debit Card No : ", debit_card.get_card_num())
print("Hermione's Account No : ",hermione_account.get_acc_id())
print("Seller : ", kfc.get_seller_name())
print("KFC's Account No : ", kfc_account.get_acc_id())
print("KFC account before paid : ",kfc_account.get_acc_balance())
print("Hermione account before paid : ",hermione_account.get_acc_balance())
edc.paid(debit_card, 500, kfc_account)
print("KFC account after paid : ",kfc_account.get_acc_balance())
print("Hermione account after paid : ",hermione_account.get_acc_balance())
print("")


#################################################
# Test Case #5
# Hermione's Account No :  0987654321
# Tops's Account No :  0000000322
# Tops account before paid :  0
# Hermione account before paid :  10500
# Tops account after paid :  500
# Hermione account after paid :  10000

hermione_account = scb.search_account_from_account_no('0987654321')
debit_card = hermione_account.get_card()
tops_account = scb.search_account_from_account_no('0000000322')
tops = scb.search_seller('Tops')
print("Test Case #5")
print("Hermione's Account No : ",hermione_account.get_acc_id())
print("Tops's Account No : ", tops_account.get_acc_id())
print("Tops account before paid : ",tops_account.get_acc_balance())
print("Hermione account before paid : ",hermione_account.get_acc_balance())
tops.paid(hermione_account,500,tops_account)
print("Tops account after paid : ",tops_account.get_acc_balance())
print("Hermione account after paid : ",hermione_account.get_acc_balance())
print("")


#################################################
# Test case #6: Display all transactions of Hermione using a `for` loop.

hermione_account = scb.search_account_from_account_no('0987654321')
for transaction in hermione_account.get_acc_transaction():
    print(transaction)