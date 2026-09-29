import math
import sys
import math, sys

# Memanggil konstanta pi
math.pi
print(math.pi)

# Memanggil fungsi sin dengan parameter pi/2
print(math.sin(math.pi / 2))

# Membuat fungsi sin sendiri tanpa mengimport modul (langkah 8)
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14
print(sin(pi / 2))