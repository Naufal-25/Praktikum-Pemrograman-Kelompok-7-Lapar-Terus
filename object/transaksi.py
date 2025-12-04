from object.pembeli import Pembeli

class Transaksi:
    def __init__(self, id_transaksi, pembeli, total=0):
        self.id_transaksi = id_transaksi
        self.pembeli = pembeli
        self.detail = []
        self.total_awal = total

    def tambah_detail(self, d):
        self.detail.append(d)
    
    def hitung_total(self):
        return sum(d.subtotal for d in self.detail)
    
    def __str__(self):
        total = self.hitung_total()
        return f"Transaksi[{self.id_transaksi}] - {self.pembeli.nama} | Total: Rp{total} | Kontak: {self.pembeli.kontak}"
    
    #simpan ke database txt
    def to_text(self):
        return f"{self.id_transaksi}|{self.pembeli.nama}|{self.pembeli.kontak}|{self.hitung_total()}"
    
    #buka dari database txt
    @staticmethod
    def from_text(line):
        id_transaksi, nama, kontak, total = line.strip().split("|")
        pembeli = Pembeli(nama, kontak)
        return Transaksi(id_transaksi, pembeli, int(float(total)))