class Bank():
    def __init__(self):
        self.__users = []
        self.__atms = []

    def get_user(self):
        return self.__users

    def get_atm(self):
        return self.__atms


class User():
    def __init__(self, user_id, user_name):
        self.__user_id = user_id
        self.__user_name = user_name
        self.__user_acc = []

    def get_user_id(self):
        return self.__user_id

    def get_user_acc(self):
        return self.__user_acc


class Account():
    def __init__(self, acc_id, acc_name, card, balance):
        self.__acc_id = acc_id
        self.__acc_name = acc_name
        self.__acc_card = card
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
        self.__acc_balance = balance

    def get_acc_transaction(self):
        return self.__acc_transaction


class Card():
    def __init__(self, num):
        self.__card_num = num
        self.__card_pin = '1234'

    def get_card_num(self):
        return self.__card_num

    def get_card_pin(self):
        return self.__card_pin


class AtmMachine():
    def __init__(self, id, balance):
        self.__atm_id = id
        self.__atm_balance = balance

    def get_atm_id(self):
        return self.__atm_id

    def get_atm_balance(self):
        return self.__atm_balance

    def set_atm_balance(self, balance):
        self.__atm_balance = balance

    def insert_card(self, bank, card, pin):
        try:
            for user in bank.get_user():
                for account in user.get_user_acc():
                    if account.get_acc_card().get_card_num() == card:
                        if account.get_acc_card().get_card_pin() == pin:
                            print(user.get_user_id())
                            print(account.get_acc_card().get_card_num())
                            print("Success")
                            print()
                            return account
                        else:
                            return "Invalid PIN"
            return "Not Found"
        except:
            return "Error"

    def deposit(self, acc, amount):
        if amount > 0:
            print(f"before: {acc.get_acc_balance()}")
            new_balance = acc.get_acc_balance() + amount
            acc.set_acc_balance(new_balance)
            self.set_atm_balance(self.get_atm_balance() + amount)
            acc.get_acc_transaction().append(f"D :{amount}-{self.get_atm_id()}")
            return f"after: {new_balance}"
        else:
            return "Error"

    def withdraw(self, acc, amount):
        try:
            if amount > 40000:
                print("Exceed Limit")
                amount = 40000
            if acc.get_acc_balance() >= amount:
                if self.get_atm_balance() >= amount:
                    print(f"before: {acc.get_acc_balance()}")
                    new_balance = acc.get_acc_balance() - amount
                    acc.set_acc_balance(new_balance)
                    self.set_atm_balance(self.get_atm_balance() - amount)
                    acc.get_acc_transaction().append(f"W :{amount}-{self.get_atm_id()}")
                    return f"after: {new_balance}"
                else:
                    print("ATM Out of Money")
            else:
                return "Error"
        except:
            print("Error")

    def transfer(self, p1, p2, amount):
        if p1.get_acc_balance() >= amount:
            print(f"{p1.get_acc_name()} before: {p1.get_acc_balance()}")
            print(f"{p2.get_acc_name()} before: {p2.get_acc_balance()}")
            p1.set_acc_balance(p1.get_acc_balance() - amount)
            p2.set_acc_balance(p2.get_acc_balance() + amount)
            p1.get_acc_transaction().append(f"TW :{amount} to {p2.get_acc_id()} - {self.get_atm_id()}")
            p2.get_acc_transaction().append(f"TD :{amount} from {p1.get_acc_id()} - {self.get_atm_id()}")
            print(f"{p1.get_acc_name()} after: {p1.get_acc_balance()}")
            return f"{p2.get_acc_name()} after: {p2.get_acc_balance()}"
        else:
            return "Error"

def find_user(bank, id):
    for i in bank.get_user():
        for j in i.get_user_acc():
            if j.get_acc_id()==id:
                return j
    return "Not Found"

## test ###
bank = Bank()

user = {'1-1101-12345-12-0': ['Harry Potter', '1234567890', '12345', 200000],
        '1-1101-12345-13-0': ['Hermione Jean Granger', '0987654321', '12346', 1000000]}

atm = {'1001': 1000000, '1002': 200000}

for i in atm:
    bank.get_atm().append(AtmMachine(i, atm[i]))

for i in user:
    bank.get_user().append(User(i, user[i][0]))
    bank.get_user()[-1].get_user_acc().append(Account(user[i][1], user[i][0], Card(user[i][2]), user[i][3]))

atm_machine = bank.get_atm()[0]

# #test1
print("Test1")
atm_machine.insert_card(bank, '12345', '1234')
print("-----------------")

#test2
print("Test2")
print(atm_machine.deposit(atm_machine.insert_card(bank, '12346', '1234'), 1000))
print("-----------------")

# #test3
print("Test3")
print(atm_machine.deposit(atm_machine.insert_card(bank, '12346', '1234'), -1))
print("-----------------")

# #test4
print("Test4")
print(atm_machine.withdraw(atm_machine.insert_card(bank, '12346', '1234'), 500))
print("-----------------")

# #test5
print("Test5")
print(atm_machine.withdraw(atm_machine.insert_card(bank, '12346', '1234'), 2000))
print("-----------------")

# #test6
print("Test6")
print(atm_machine.transfer(atm_machine.insert_card(bank, '12345', '1234'), find_user(bank, '0987654321'), 1000))
print("-----------------")

# #test7
print("Test7")
key = find_user(bank, '0987654321')
print(key.get_acc_transaction())
print("-----------------")

# #test8
print("Test8")
print(atm_machine.insert_card(bank, '12346', '1345'))
print("-----------------")

# #test9
print("Test9")
print(atm_machine.withdraw(atm_machine.insert_card(bank, '12346', '1234'), 41000))
print("-----------------")

# #test10
print("Test10")
print(atm_machine.withdraw(atm_machine.insert_card(bank, '0987654321', '12346'), 41000))
print("-----------------")