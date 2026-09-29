"""Eksepsi Bertingkat untuk Pembagian dengan Nol"""
try:
  bil1 = 9
  bil2 = 0
  x = bil1 / bil2
except IndexError:
  print("Ada kesalahan indeks")
except ZeroDivisionError:
  print("Ada kesalahan pembagian 0")

print("<< End Program >>")

"""Eksepsi Bertingkat untuk Akses List di Luar Batas"""
try:
  list = [1, 2, 3]
  print(list[3])
except ZeroDivisionError:
  print("Operasi tidak bisa dijalankan")
except IndexError:
  print("Ada kesalahan indeks")

print("<< End Program >>")

"""Menggunakan ZeroDivisionError dan Base Exception (except:)"""
try:
  list = [1, 2, 3]
  print(list[3])
except ZeroDivisionError:
  print("Operasi tidak bisa dijalankan")
except:
  print("Ada kesalahan ")

print("<< End Program >>")

"""Urutan LookupError di Atas IndexError"""
try:
  list = [1, 2, 3]
  print(list[3])
except LookupError:
  print("Ada kesalahan")
except IndexError:
  print("Ada kesalahan indeks")
except:
  print("Ada kesalahan ")

print("<< End Program >>")

"""Urutan IndexError di Atas LookupError (Benar/Spesifik ke Umum)"""
try:
  list = [1, 2, 3]
  print(list[3])
except IndexError:
  print("Ada kesalahan indeks")
except LookupError:
  print("Ada kesalahan")
except:
  print("Ada kesalahan ")

print("<< End Program >>")

"""Urutan ArithmeticError di Atas ZeroDivisionError"""
try:
  bil1 = 9
  bil2 = 0
  x = bil1 / bil2
except ArithmeticError:
  print("Ada kesalahan aritmatika")
except FloatingPointError:
  print("Ada kesalahan floating point")
except ZeroDivisionError:
  print("Ada pembagian dengan 0")

print("<< End Program >>")

"""Urutan Spesifik (ZeroDivisionError) di Atas Induk (ArithmeticError)"""
try:
  bil1 = 9
  bil2 = 0
  x = bil1 / bil2
except FloatingPointError:
  print("Ada kesalahan floating point")
except ZeroDivisionError:
  print("Ada pembagian dengan 0")
except ArithmeticError:
  print("Ada kesalahan aritmatika")

print("<< End Program >>")