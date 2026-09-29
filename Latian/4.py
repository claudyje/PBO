class persegi_pjg():
    def __init__(self, p, l):
        if p <= 0 or l <=0:
            raise ValueError("Nilai panjang dan lebar tidak boleh sama dengan nol/bilangan negatif")
        self.p = p
        self.l = l

    def hitung_luas(self):
        return self.p*self.l

try:
    persegi = persegi_pjg(4,5)
    print(f"luas persegi panjang = 4 dan lebar = 5 adalah {persegi.hitung_luas()}")
except ZeroDivisionError:
    print("Salah satu angka tidak boleh 0")


print()
class produk():
    def __init__(self,nama,harga):
        self.nama = nama
        self.harga = harga
class keranjang():
    def __init__(self):
        self.__item = []
    def tambah_produk(self,produk):
        self.__item.append(produk)
        print(f"Berhasil menambahkan {produk.nama} ke keranjang")
    def hitung(self):
        total = 0 
        for item in self.__item:
            total += item.harga
        return total
        
prod1 = produk("Buku Tulis", 5000)
prod2 = produk("Pulpen Gel", 3000)
prod3 = produk("Tas Ransel", 150000)
keranjangku = keranjang()
keranjangku.tambah_produk(prod1)
keranjangku.tambah_produk(prod2)
keranjangku.tambah_produk(prod3)
print(f"Total belanjaan Anda: Rp. {keranjangku.hitung()}")

print()
"""Studi Kasus:Buatlah program berbasis objek dengan 2 kelas:
1. Kelas Mahasiswa:Memiliki atribut private __nama dan __ipk.   
Gunakan konstruktor untuk mengisi data awal, dengan validasi (error handling): jika IPK yang dimasukkan < 0.0 atau > 4.0, maka raise ValueError("IPK tidak valid!").   Buat method getter (get_nama(), get_ipk()) untuk mengakses atribut private tersebut.   
2. Kelas PortalAkademik:Memiliki method cek_status_kelulusan(mahasiswa) yang menerima objek Mahasiswa, 
lalu mencetak apakah mahasiswa tersebut lulus dengan pujian (Cumlaude jika IPK >= 3.5) atau tidak."""
class mahasiswa():
    def __init__(self, nama, ipk):
        if ipk<0.0 and ipk>4.0:
            raise ValueError("Nilai yang anda masukkan tidak valid")
        self.__nama = nama
        self.__ipk = ipk
    def get_nama(self):
        return self.__nama
    def get_ipk(self):
        return self.__ipk

class portal_akademik():
    def cek_status_lulus(self, mhs):
        ipk = mhs.get_ipk()
        nama = mhs.get_nama()
        print(f"Nama mahasiswa = {nama} | ipk = {ipk}")
        if ipk >= 3.5:
            print("Selamat anda lulus dengan predikat cumlaude")
        else:
            print("Selamat anda lulus dengan baik")

try:
    mhs1 = mahasiswa('JESSIE', 4.00)
    portal = portal_akademik()
    portal.cek_status_lulus(mhs1)
except ValueError as e:
    print(f"Gagal memuat data mahasiswa: {e}")


