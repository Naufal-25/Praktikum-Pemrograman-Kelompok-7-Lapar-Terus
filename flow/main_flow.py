from flow.menu_makanan import menu_makanan
from flow.menu_pesanan import menu_pesanan

def main():
    daftar_makanan = []
    daftar_transaksi = []
    pembeli = pembeli("P001", "Pengunjung", "-")
    while True:
        print("\n=== SISTEM KANTIN ===")
        print("1. Kelola Makanan")
        print("2. Kelola Pesanan")
        print("3. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            menu_makanan(daftar_makanan)
        elif pilihan == "2":
            menu_pesanan(daftar_transaksi, daftar_makanan, pembeli)
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem kantin.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
