import game.image.change
import game.image.close
import game.image.open

import game.level.load
import game.level.over
import game.level.start

import game.sound.load
import game.sound.pause
import game.sound.play

def main():
    while True:
        print("\n==============================")
        print("      MENU UTAMA PROGRAM      ")
        print("==============================")
        print("[1] Menu Modul Image")
        print("[2] Menu Modul Level")
        print("[3] Menu Modul Sound")
        print("[0] Keluar")
        
        pilihan = input("Pilih menu (0-3): ")
        
        if pilihan == "1":
            print("\n--- Modul Image ---")
            print(game.image.change.function1())
            print(game.image.close.function2())
            print(game.image.open.function3())
            
        elif pilihan == "2":
            print("\n--- Modul Level ---")
            pilihan = input("Pilih menu (1-3) = ")
            if pilihan ==    "1":
                print(game.level.load.function4())
            elif pilihan == "2":
                print(game.level.over.function5())
            elif pilihan == "3":
                print(game.level.start.function6())
            else:
                print("Pilihan tidak valid")
            
        elif pilihan == "3":            
            print("\n--- Modul Sound ---")
            pilihan = input("Pilih menu (1-3) = ")
            if pilihan ==    "1":
                print(game.sound.load.function7())
            elif pilihan == "2":
                print(game.sound.pause.function8())
            elif pilihan =="3":
                print(game.sound.play.pilih_sound())
            else:
                print("Pilihan tidak valid")
            
        elif pilihan == "0":
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()

