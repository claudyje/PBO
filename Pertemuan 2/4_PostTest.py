import HitungBangun.luas.persegi
import HitungBangun.luas.lingkaran
import HitungBangun.volume.kubus
import HitungBangun.volume.tabung

def main():
    while True:
        print("\n==================================")
        print("   PROGRAM HITUNG BANGUN RUANG   ")
        print("==================================")
        print("Pilihan Menu:")
        print("1. Hitung Luas")
        print("2. Hitung Volume")
        print("0. Keluar")
        
        menu = input("Masukkan pilihan menu (1/2/0): ")
        
        if menu == "1":
            print("\n--- MENU LUAS ---")
            print("1. Luas Persegi")
            print("2. Luas Lingkaran")
            sub_menu = input("Pilih jenis luas (1/2): ")
            
            if sub_menu == "1":
                sisi = float(input("Masukkan panjang sisi persegi: "))
                hasil = HitungBangun.luas.persegi.persegi(sisi)
                print("Hasil Luas Persegi =", hasil)
            elif sub_menu == "2":
                jari = float(input("Masukkan panjang jari-jari lingkaran: "))
                hasil = HitungBangun.luas.lingkaran.lingkaran(jari)
                print("Hasil Luas Lingkaran =", hasil)
            else:
                print("Pilihan tidak valid!")
                
        elif menu == "2":
            print("\n--- MENU VOLUME ---")
            print("1. Volume Kubus")
            print("2. Volume Tabung")
            sub_menu = input("Pilih jenis volume (1/2): ")
            
            if sub_menu == "1":
                sisi = float(input("Masukkan panjang sisi kubus: "))
                hasil = HitungBangun.volume.kubus.kubus(sisi)
                print("Hasil Volume Kubus =", hasil)
            elif sub_menu == "2":
                jari = float(input("Masukkan jari-jari alas tabung: "))
                tinggi = float(input("Masukkan tinggi tabung: "))
                hasil = HitungBangun.volume.tabung.tabung(jari, tinggi)
                print("Hasil Volume Tabung =", hasil)
            else:
                print("Pilihan tidak valid!")
                
        elif menu == "0":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan menu tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()