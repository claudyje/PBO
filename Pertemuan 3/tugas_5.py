""" MEMBUAT ATM SEDERHANA"""
saldo = 100000000
while True:
    print("------SELAMAT DATANG DI ATM SEJAHTERA------")
    print("1. TARIK TUNAI")
    print("2. LIHAT SALDO" )
    pilih = (input("Masukkan pilihan anda :"))
    if pilih == "1":
        try:
            uang = int(input("Masukkan nominal anda = Rp."))
            if uang > saldo:
                print("MAAF SALDO ANDA KURANG")
            elif uang <= 0:
                print("MAAF TIDAK VALID... NOMINAL HARUS DIATAS Rp.0")
            else:
                saldo -= uang
                print("SILAHKAN TUNGGU UANG ANDA... TERIMA KASIH")
                print("Sisa saldo anda Rp.", saldo)
        except ValueError:
            print("Input tidak valid")
    elif pilih == "2":
        print("SALDO ANDA SEBESAR Rp.", saldo)
    else:
        print("Terima Kasih")
        break