angka = [10,20,0]
try:
    pembagi = angka[3]
    hasil = 100/pembagi
    print(hasil)
except IndexError:
    print("Angka diluar indeks")
except ZeroDivisionError:
    print("Pembagian dengan nol")