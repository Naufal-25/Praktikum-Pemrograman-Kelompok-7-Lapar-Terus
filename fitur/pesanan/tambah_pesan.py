from object.detail import Detail
from object.transaksi import Transaksi
from object.pembeli import Pembeli
from fitur.makanan.datamanage_makanan import save_makanan
from fitur.pesanan.datamanage_pesan import save_transaksi
from fitur.pesanan.datamanage_detail import save_detail

def tambah_pesanan(daftar_transaksi, daftar_makanan, pembeli):
    print("\n=== Tambah Pesanan ===")
    id_transaksi = input("ID Transaksi: ")

    transaksi = None
    for t in daftar_transaksi:
        if t.id_transaksi == id_transaksi:
            transaksi = t
            break

    if not transaksi:
        print("\n=== Data Pembeli ===")
        id_pembeli = input("ID Pembeli: ")
        nama = input("Nama Pembeli: ")
        kontak = input("Kontak: ")

        pembeli = Pembeli(id_pembeli, nama, kontak)
        transaksi = Transaksi(id_transaksi, pembeli)
        daftar_transaksi.append(transaksi)

    id_makanan = input("Masukkan ID makanan: ")

    makanan_obj = None
    for m in daftar_makanan:
        if m.id_makanan == id_makanan:
            makanan_obj = m
            break
    
    if not makanan_obj:
        print("Makanan tidak ditemukan\n")
        return
    
    try:
        jumlah = int(input("Jumlah: "))
    except ValueError:
        print("Jumlah harus angka!")
        return
    
    if jumlah <= 0:
        print("Jumlah harus lebih dari 0")
        return
    
    if jumlah > makanan_obj.stok:
        print("Stok tidak cukup!")
        return
    
    makanan_obj.stok -= jumlah
    save_makanan(daftar_makanan)

    id_detail = input("Masukkan ID detail pesanan: ")
    
    subtotal = makanan_obj.harga * jumlah

    n_detail = Detail(id_detail,id_transaksi,makanan_obj.id_makanan,makanan_obj,jumlah,subtotal)

    transaksi.tambah_detail(n_detail)

    save_transaksi(daftar_transaksi)
    save_detail(daftar_transaksi)

    print(f"Pesanan {makanan_obj.nama} berhasil ditambahkan.\n")