print('ini teks dari modul')
print(__name__)

if __name__ == '__main__':
    print('Anda menjalankan module.py')
else:
    print('Anda mengimport modul')

counter = 0

def jumlahkan(lst):
    hasiljml = 0
    for element in lst:
        hasiljml += element
    return hasiljml