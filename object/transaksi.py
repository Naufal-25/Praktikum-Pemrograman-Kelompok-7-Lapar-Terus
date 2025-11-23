from pembeli import Pembeli

class Transaksi:
    def __init__(self, id_transaksi, pembeli, status="Belum Bayar"):
        self.id_transaksi = id_transaksi
        self.pembeli = pembeli
        self.detail = []
        self.status = status

    def tambah_detail(self, d):
        self.detail.append(d)
    
    def total(self):
        return sum(d.subtotal for d in self.detail)
    
    def __str__(self):
        total = self.total()
        return f"Transaksi[{self.id_transaksi}] - {self.pembeli.nama}({self.pembeli.kontak}) | Total: Rp{total} | Status: {self.status} Kontak: {self.pembeli.kontak}"
    
    #simpan ke database txt
    def to_text(self):
        return f"{self.id_transaksi},{self.pembeli.id_pembeli},{self.pembeli.nama},{self.pembeli.kontak},{self.status}"
    
    #buka dari database txt
    @staticmethod
    def from_text(line):
        id_transaksi, id_pembeli, nama, kontak, status = line.strip().split(",")
        pembeli = Pembeli(id_pembeli, nama, kontak)
        return Transaksi(id_transaksi, pembeli, status)