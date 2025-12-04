from flow.menu_makanan import menu_makanan
from flow.menu_pesanan import menu_pesanan
from fitur.makanan.datamanage_makanan import load_makanan
from fitur.pesanan.datamanage_pesan import load_transaksi
from fitur.pesanan.datamanage_detail import load_detail

def main():
    try:
        daftar_makanan = load_makanan()
        daftar_transaksi = load_transaksi()
        load_detail(daftar_transaksi, daftar_makanan)
        print("Database berhasil dimuat")
    except Exception as e:
        print(f"Gagal memuat database. error:{e}") 
        daftar_makanan = []
        daftar_transaksi = []
    while True:
        print("\n=== SISTEM KANTIN ===")
        print("1. Kelola Makanan")
        print("2. Kelola Pesanan")
        print("3. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            menu_makanan(daftar_makanan)
        elif pilihan == "2":
            menu_pesanan(daftar_transaksi, daftar_makanan)
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem kantin.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
