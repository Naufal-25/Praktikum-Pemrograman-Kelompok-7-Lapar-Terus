from fitur.makanan.datamanage_makanan import save_makanan
from fitur.pesanan.datamanage_pesan import save_transaksi
from fitur.pesanan.datamanage_detail import save_detail

def bayar_pesanan(daftar_transaksi, daftar_makanan):
    print("\n=== Pembayaran (Kasir) ===")
    id_transaksi = input("Masukkan ID transaksi: ").strip()

    index_target = -1
    for i, t in enumerate(daftar_transaksi):
        if t.id_transaksi == id_transaksi:
            index_target = i
            break

    if index_target == -1:
        print("Transaksi tidak ditemukan.")
        return
    
    transaksi = daftar_transaksi[index_target]
    total_tagihan = transaksi.hitung_total()

    print("\n"+"="*30)
    print(f"Tagihan : {transaksi.pembeli.nama}")
    print(f"Total   : Rp{total_tagihan}")
    print("="*30)
    try:
        uang = float(input("Uang Tunai: Rp "))
    except ValueError:
        print("Input uang tidak valid")
    
    if uang < total_tagihan:
        kurang = total_tagihan - uang
        print(f"Uang kurang: Rp {kurang}")
    else:
        kembalian =  uang - total_tagihan
        print(f"Kembalian : Rp {kembalian}")
        print("\n--- Pembayaran Lunas ---")
    
    daftar_transaksi.pop(index_target)

    save_makanan(daftar_makanan)
    save_transaksi(daftar_transaksi)
    save_detail(daftar_transaksi)

    print(f"\nTransaksi {id_transaksi} berhasil diselesaikan")
    