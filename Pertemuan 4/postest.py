class Bank:
    def __init__(self, code, address):
        self.code = code
        self.address = address

    def getAccounts(self):
        print('Bank',self.code,'memiliki account')

class Customer:
    def __init__(self, name, address, dob, card_number, pin):
        self.name = name
        self.address = address
        self.dob = dob
        self.card_number = card_number
        self.pin = pin

    def verifyPassword(self, pin):
        return self.pin == pin

class Account:
    def __init__(self, number):
        self.number = number
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            print(f"Saldo di rekening {self.number} tidak mencukupi.")
            return self.balance

class ATM:
    def __init__(self, location):
        self.location = location
        self.managedby = 'admin'

    def withdraw(self,amount):
        self.balance -= amount
        return self.balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance

    def checkBalance(self):
        print("Mengecek saldo melalui",self.location)
    
class ATMTransactions:
    def __init__(self, transaction_id, date, type, amount, post_balance):
        self.transaction_id = transaction_id
        self.date = date
        self.type = type
        self.amount = amount
        self.post_balance = post_balance

    def modifies(self):
        print("Transaksi", self.transaction_id, "berhasil")
        print("Tipe:", self.type)
        print("Jumlah: Rp", self.amount)
        print("Saldo akhir: Rp", self.post_balance)


#OBJEK
cust1 = Customer('Jessie','Korea','',111222,'jessie#')
print(cust1.verifyPassword('jess#'))
