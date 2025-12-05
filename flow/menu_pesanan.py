from fitur.pesanan.tambah_pesan import tambah_pesanan
from fitur.pesanan.baca_pesan import baca_pesanan
from fitur.pesanan.ubah_pesan import ubah_pesanan
from fitur.pesanan.hapus_pesan import hapus_pesanan
from fitur.pesanan.bayar_pesan import bayar_pesanan

def menu_pesanan(daftar_transaksi, daftar_makanan):
    while True:
        print("\n=== MENU PESANAN ===")
        print("1. Tambah Pesanan")
        print("2. Lihat Pesanan")
        print("3. Ubah Pesanan")
        print("4. Batalkan Pesanan")
        print("5. Bayar Pesanan")
        print("0. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_pesanan(daftar_transaksi, daftar_makanan, None)
        elif pilihan == "2":
            baca_pesanan(daftar_transaksi)
        elif pilihan == "3":
            ubah_pesanan(daftar_transaksi, daftar_makanan)
        elif pilihan == "4":
            hapus_pesanan(daftar_transaksi, daftar_makanan)
        elif pilihan == "5":
            bayar_pesanan(daftar_transaksi, daftar_makanan)
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.")
