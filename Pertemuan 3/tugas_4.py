"""overflowerror > arithmaticerror > exception"""
try:
  # Memicu OverflowError (misal eksponensial angka sangat besar)
  import math

  x = math.exp(1000)
except OverflowError as e:
  print("Tertangkap OverflowError:", e)
except ArithmeticError as e:
  print("Tertangkap ArithmeticError:", e)
except Exception as e:
  print("Tertangkap Exception umum:", e)

print("<< End Program >>")

"""FileExistsError > OSError > Exception."""
try:
  # Asumsikan file 'sample.txt' sudah ada, lalu kita paksa buat dengan mode 'x' (exclusive creation)
  with open("sample.txt", "x") as f:
    f.write("halo")
except FileExistsError as e:
  print("Tertangkap FileExistsError:", e)
except OSError as e:
  print("Tertangkap OSError:", e)
except Exception as e:
  print("Tertangkap Exception umum:", e)

print("<< End Program >>")


"""ZipImportError > ImportError > Exception"""
import zipimport

try:
  # Memaksa zipimporter pada file yang bukan zip atau tidak valid
  importer = zipimport.zipimporter("file_bukan_zip.zip")
  importer.load_module("modul_palsu")
except zipimport.ZipImportError as e:
  print("Tertangkap ZipImportError:", e)
except ImportError as e:
  print("Tertangkap ImportError:", e)
except Exception as e:
  print("Tertangkap Exception umum:", e)

print("<< End Program >>")