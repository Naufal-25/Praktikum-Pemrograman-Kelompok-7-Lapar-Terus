def baca_pesanan(daftar_transaksi):
    print("\n=== Daftar Transaksi & Detail ===")
    if not daftar_transaksi:
        print("Belum ada transaksi.")
        return
    
    for t in daftar_transaksi:
        print("\n"+"="*40)
        print(f"ID: {t.id_transaksi}")
        print(f"Pembeli: {t.pembeli.nama} ({t.pembeli.kontak})")
        print("-"*40)

    if not t.detail:
        print("(Kosong)")
    else:
        for d in t.detail:
            nama_menu = d.makanan.nama if d.makanan else "Menu Terhapus"
            print(f"-{nama_menu:<15} x {d.jumlah:<3} = Rp{d.subtotal}")
    
    print("-"*40)
    print(f"Total Tagihan: Rp{t.hitung_total()}")
    print("="*40)
    print()