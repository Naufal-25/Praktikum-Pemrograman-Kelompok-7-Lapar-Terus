from object.pembeli import Pembeli

class Transaksi:
    def __init__(self, id_transaksi, pembeli, status="Belum Bayar", total=0):
        self.id_transaksi = id_transaksi
        self.pembeli = pembeli
        self.detail = []
        self.status = status
        self.total_awal = total

    def tambah_detail(self, d):
        self.detail.append(d)
    
    def hitung_total(self):
        return sum(d.subtotal for d in self.detail)
    
    def __str__(self):
        total = self.hitung_total()
        return f"Transaksi[{self.id_transaksi}] - {self.pembeli.nama} | Total: Rp{total} | Status: {self.status} Kontak: {self.pembeli.kontak}"
    
    #simpan ke database txt
    def to_text(self):
        return f"{self.id_transaksi},{self.pembeli.id_pembeli},{self.pembeli.nama},{self.pembeli.kontak},{self.status},{self.hitung_total()}"
    
    #buka dari database txt
    @staticmethod
    def from_text(line):
        id_transaksi, id_pembeli, nama, kontak, status, total = line.strip().split(",")
        pembeli = Pembeli(id_pembeli, nama, kontak)
        return Transaksi(id_transaksi, pembeli, status)