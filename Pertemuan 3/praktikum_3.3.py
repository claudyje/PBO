""" eror karena aritmatika pembagian dengan angka nol"""
bil1 = 9
bil2 = 0 
# x = bil1/bil2
# print("<<End Program>>")

try:
    bil1 = 9
    bil2 = 0
    x= bil1/bil2
except Exception as e:
    print(e)
print("<<End Program>>")

""" eror karena modul math tidak ada konten a"""
import math
try:
    print(math.a)
except Exception as e:
    print(e)
print("<<End Program>>")

""" eror karena modul time tidak ada datetime"""
# from time import datetime
# print("<<End Program>>")

try:
    from time import datetime
except Exception as e:
    print(e)
print("<<End Program>>")

""" eror karena tidak ada modul bernama mymodul"""
# import mymodul
# print("<<End Program>>")

try:
    import mymodul
except Exception as e:
    print(e)
print("<<End Program>>")

""" eror karena indeks out of range"""
# list = [1,2,3]
# print(list[3])
# print("<<End Program>>")

try:
    list = [1,2,3]
    print(list[3])
except Exception as e:
    print(e)
print("<<End Program>>")

""" eror karena key anggur tidak ada"""
# harga = {"apel": 25000, "jeruk": 20000, "mangga":15000 }
# harga["anggur"]
# print("<<End Program>>")
try:
    harga = {"apel": 25000, "jeruk": 20000, "mangga":15000 }
    harga["anggur"]
except Exception as e:
    print(e)
print("<<End Program>>")

""" eror karena list kosong"""
# list = []
# x = max(list)
# print("<<End Program>>")
try:
    list=[]
    x=max(list)
except Exception as e:
    print(e)
print("<<End Program>>")

""" eror karena variabel tidak terdefinisi"""
# text='Halo mari belajar eksepsi'
# print(teks)
# print("<<End Program>>")

try:
    text='Halo mari belajar eksepsi'
    print(teks)
except Exception as e:
    print(e)
print("<<End Program>>")

"""eror karena string dan int tidak bisa ditambahkan"""
# varString = "Hello"
# varInt = 100
# print( varString + varInt)
# print("<<End Program>>")

try:
    varString = "Hello"
    varInt = 100
    print( varString + varInt)
except Exception as e:
    print(e)
print("<<End Program>>")

"""eror karena file tidak ditemukan"""
# with open("sample.txt, mode="r"") as file:
#     print(file.read())
# print("<<End Program>>")
try:
    with open("sample.txt, mode="r"") as file:
        print(file.read())
except Exception as e:
    print(e)
print("<<End Program>>")

