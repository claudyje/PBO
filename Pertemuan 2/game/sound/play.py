def pilih_sound():
    # Daftar pilihan sound yang tersedia
    daftar_sound = [
        "Change Wolrd.mp3",
        "Bersamamu.mp3",
        "Hujan.mp3",
        "Rindu.mp3"
    ]
    
    print("=== PILIH SOUND ===")
    # Menampilkan pilihan menggunakan perulangan
    for i in range(len(daftar_sound)):
        print(f"{i + 1}. {daftar_sound[i]}")
        
    try:
        # Meminta input pilihan dari pengguna
        pilihan = int(input("Masukkan nomor pilihan sound (1-4): "))
        
        # Validasi pilihan agar sesuai dengan rentang indeks
        if 1 <= pilihan <= len(daftar_sound):
            sound_terpilih = daftar_sound[pilihan - 1]
            print(f"Berhasil memilih: {sound_terpilih}")
            return sound_terpilih
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
            return None
    except ValueError:
        print("Harap masukkan angka yang valid!")
        return None

