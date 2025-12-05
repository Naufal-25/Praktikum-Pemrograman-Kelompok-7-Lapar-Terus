def baca_pesanan(daftar_transaksi):
    print("\n=== Daftar Transaksi & Detail ===")
    if not daftar_transaksi:
        print("Belum ada transaksi.")
        return
    
    for t in daftar_transaksi:
        print("="*40)
        nama_pembeli = t.pembeli.nama if t.pembeli else "Tanpa Nama"
        kontak_pembeli = t.pembeli.kontak if t.pembeli else "-"

        print(f"ID: {t.id_transaksi}")
        print(f"Pembeli: {nama_pembeli} ({kontak_pembeli})")
        print("-"*40)

        if not t.detail:
            print("(Kosong)")
        else:
            for d in t.detail:
                print(f" - {d}")
    
        print("-"*40)
        print(f"Total Tagihan: Rp{t.hitung_total()}")
        print("="*40)
        print()