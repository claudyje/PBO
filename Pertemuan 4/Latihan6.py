class kendaraan:
    def __init__(self):
        self.__jenis = ''
        self.__merk = ''
        self.__nama = ''
        self.__warna = ''

    def set_atribut(self,val1='', val2='',val3='', val4=''):
        self.__jenis = val1
        self.__merk = val2
        self.__nama = val3
        self.__warna = val4


    def get_atribut(self):
        print("Jenis \t:",self.__jenis,
              "\nMerk \t: ",self.__merk,
              "\nNama \t: ",self.__nama,
              "\nWarna \t: ",self.__warna)
    

bmw = kendaraan()
bmw.set_atribut('Mobil','BMW','BMW M4','Hitam')
bmw.get_atribut()
print()
brio = kendaraan()
brio.set_atribut(val1 ='mobil',val4 = 'merah')
brio.get_atribut()
print()
vario = kendaraan()
vario.set_atribut(val2 ='Honda',val4 = 'hitam')
vario.get_atribut()


