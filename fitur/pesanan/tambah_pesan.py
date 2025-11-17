from object.detail import Detail
from object.transaksi import Transaksi

def tambah_pesanan(daftar_transaksi, daftar_makanan, pembeli):
    print("\n=== Tambah Pesanan ===")
    id_transaksi = input("ID Transaksi: ")

    transaksi = None
    for t in daftar_transaksi:
        if t.id_transaksi == id_transaksi:
            transaksi = t
            break

    if not transaksi:
        transaksi = Transaksi(id_transaksi, pembeli)
        daftar_transaksi.append(transaksi)

    id_makanan = input("Masukkan ID makanan: ")
    for makanan in daftar_makanan:
        if makanan.id_makanan == id_makanan:
            jumlah = int(input("Jumlah: "))
            if jumlah > makanan.stok:
                print("Stok tidak cukup!")
                return
            
            makanan.stok -= jumlah
            id_detail = f"D{len(transaksi.detail)+1:03d}"
            detail_baru = Detail(id_detail, transaksi, makanan, jumlah)
            transaksi.tambah_detail(detail_baru)
            print(f"Pesanan {makanan.nama} berhasil ditambahkan ke transaksi {id_transaksi}\n")
            return
        
    print("Makanan tidak ditemukan.\n")

