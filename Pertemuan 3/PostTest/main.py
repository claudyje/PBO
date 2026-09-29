from kalkulator import tambah, kurang, perkalian, pembagian

Operasi = {
      1 :tambah,
      2 : kurang,
      3 : perkalian,
      4 : pembagian
}

while True:
    try:
        bil1 = int(input("Angka pertama : "))
        bil2 = int(input("Angka Kedua   : "))
        print("1. Tambah")
        print("2. Kurang")
        print("3. Kali")
        print("4. Bagi")
        pilih = int(input("Masukkan pilihan : "))
        hasil = Operasi[pilih](bil1, bil2)
        print("Hasil = ", hasil)
    except ValueError:
        print("Masukkan angka bukan huruf")
    except ZeroDivisionError:
        if pilih == 4 and bil2 == 0:
            print("Bilangan 2 adalah angka 0... pembagian tidak bisa berjalan")
    except KeyError:
        print("pilhan tidak valid")
    tanya = input("Mau lanjut? (y/n): ")
    if tanya == 'n' or tanya == 'N':
        break

    
