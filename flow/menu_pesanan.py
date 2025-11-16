from fitur.pesanan.tambah_pesan import tambah_pesanan
from fitur.pesanan.baca_pesan import tampilkan_pesanan
from fitur.pesanan.ubah_pesan import ubah_pesanan
from fitur.pesanan.hapus_pesan import hapus_pesanan

def menu_pesanan():
    while True:
        print("\n=== MENU PESANAN ===")
        print("1. Tambah Pesanan")
        print("2. Lihat Pesanan")
        print("3. Ubah Pesanan")
        print("4. Hapus Pesanan")
        print("5. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_pesanan()
        elif pilihan == "2":
            tampilkan_pesanan()
        elif pilihan == "3":
            ubah_pesanan()
        elif pilihan == "4":
            hapus_pesanan()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid.")
