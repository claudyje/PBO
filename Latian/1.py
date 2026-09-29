class AkunBank():
    def __init__(self, saldo=0):
        self.__saldo = saldo
    def get_saldo(self):
        return self.__saldo
    def tarik_tunai(self, uang):
        if uang > self.__saldo:
            raise ValueError ("Jumlah tarik tunai melebihi saldo")
        self.__saldo -= uang
        return self.__saldo
    def setor_tunai(self, uang):
        self.__saldo += uang
        return self.__saldo
    
akun = AkunBank(90000)
print (f"Saldo anda sebesar Rp.{akun.get_saldo()}")
print (f"Tarik tunai berhasil, saldo anda sekarang Rp.{akun.tarik_tunai(50000)}")
print(f"Setor tunai berhasil saldo anda sekarang Rp.{akun.setor_tunai(100000)}")
