# Sistem Toko Sederhana

# Inisialisasi daftar produk dan harga
produk = {
    1: {"nama": "Buku", "harga": 10000},
    2: {"nama": "Pensil", "harga": 2000},
    3: {"nama": "Penghapus", "harga": 1000},
    4: {"nama": "Penggaris", "harga": 5000}
}

# Fungsi untuk menampilkan daftar produk
def tampilkan_produk():
    print("Daftar Produk:")
    for kode, item in produk.items():
        print(f"{kode}. {item['nama']} - Rp{item['harga']}")

# Inisialisasi keranjang belanja
keranjang = {}

# Loop pemilihan produk
while True:
    tampilkan_produk()
    
    # Input pilihan produk
    pilihan = int(input("Masukkan kode produk (0 untuk selesai): "))
    if pilihan == 0:
        break
    
    if pilihan in produk:
        jumlah = int(input(f"Masukkan jumlah {produk[pilihan]['nama']} yang dibeli: "))
        
        # Tambahkan ke keranjang
        if pilihan in keranjang:
            keranjang[pilihan] += jumlah
        else:
            keranjang[pilihan] = jumlah
    else:
        print("Produk tidak ditemukan.")

# Hitung total pembelian
total = 0
print("\nStruk Pembelian:")
for kode, jumlah in keranjang.items():
    nama = produk[kode]['nama']
    harga = produk[kode]['harga']
    subtotal = harga * jumlah
    total += subtotal
    print(f"{nama} x {jumlah}: Rp{subtotal}")

print(f"\nTotal Pembelian: Rp{total}")
