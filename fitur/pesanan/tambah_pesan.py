from object.detail import Detail
from object.transaksi import Transaksi
from object.pembeli import Pembeli
from fitur.makanan.datamanage_makanan import save_makanan
from fitur.makanan.baca_makanan import baca_makanan
from fitur.pesanan.datamanage_pesan import save_transaksi
from fitur.pesanan.datamanage_detail import save_detail

def tambah_pesanan(daftar_transaksi, daftar_makanan, pembeli):
    print("\n=== Tambah Pesanan ===")
    id_transaksi = input("ID Transaksi: ").strip()
    if not id_transaksi:
        print("ID tidak boleh kosong")
        return

    transaksi = None
    for t in daftar_transaksi:
        if t.id_transaksi == id_transaksi:
            transaksi = t
            break

    if not transaksi:
        print("\n=== Data Pembeli ===")
        nama = input("Nama Pembeli: ").strip()
        kontak = input("Kontak: ").strip()

        pembeli = Pembeli(nama, kontak)
        transaksi = Transaksi(id_transaksi, pembeli)
        daftar_transaksi.append(transaksi)
    else:
        print(f"Melanjutkan pesanan untuk: {transaksi.pembeli.nama}\n")

    baca_makanan(daftar_makanan)

    id_makanan = input("Masukkan ID makanan: ")

    makanan_obj = None
    for m in daftar_makanan:
        if m.id_makanan == id_makanan:
            makanan_obj = m
            break
    
    if not makanan_obj:
        print("Makanan tidak ditemukan\n")
        return
    
    print(f"Dipilih: {makanan_obj.nama} (Stok: {makanan_obj.stok})")
    
    try:
        jumlah = int(input("Jumlah pesan: "))
    except ValueError:
        print("Jumlah harus angka!")
        return
    
    if jumlah <= 0:
        print("Jumlah harus lebih dari 0")
        return
    
    if jumlah > makanan_obj.stok:
        print(f"Stok tidak cukup! Stok Tersedia: {makanan_obj.stok}")
        return
    
    makanan_obj.stok -= jumlah
    subtotal = makanan_obj.harga * jumlah

    urutan =  len(transaksi.detail) + 1
    id_detail = f"{id_transaksi}-{urutan}"

    detail_baru = Detail(id_detail, id_transaksi, makanan_obj.id_makanan, makanan_obj, jumlah, subtotal)
    transaksi.tambah_detail(detail_baru)

    save_makanan(daftar_makanan)
    save_transaksi(daftar_transaksi)
    save_detail(daftar_transaksi)

    print(f"\nPesanan {makanan_obj.nama} x {jumlah} berhasil ditambahkan.")