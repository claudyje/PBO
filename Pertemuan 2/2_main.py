# Mengimpor konstanta dan fungsi dari modul yang telah dibuat[cite: 1]
from my_module import x, y, z, text, tambah, bagi, greeting

# Menampilkan nilai konstanta dan string
print("Nilai x:", x, ", y:", y, ", z:", z)
print(text)

# Menguji fungsi tambah
hasil_tambah = tambah(50, 50)
print("Hasil tambah:", hasil_tambah)

# Menguji fungsi bagi
hasil_bagi = bagi(y, z)
print("Hasil bagi:", hasil_bagi)

# Menguji fungsi greeting
pesan = greeting("Sobat")
print(pesan)

