def baca_pesanan(daftar_transaksi):
    print("\n=== Daftar Transaksi & Detail ===")
    if not daftar_transaksi:
        print("Belum ada transaksi.")
        return
    for t in daftar_transaksi:
        print(t)
        for d in t.detail:
            print(f"   - {d}")
