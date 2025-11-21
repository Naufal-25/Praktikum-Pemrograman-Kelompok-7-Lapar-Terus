class Pembeli:
    def __init__(self, id_pembeli, nama, kontak):
        self.id_pembeli = id_pembeli
        self.nama = nama
        self.kontak = kontak
    
    def __str__(self):
        return f"{self.nama} ({self.kontak})"
    
    #simpan ke database txt
    def to_text(self):
        return f"{self.id_pembeli},{self.nama},{self.kontak}"
    
    #baca dari database txt
    @staticmethod
    def from_text(line):
        id_pembeli, nama, kontak = line.strip().split(",")
        return Pembeli(id_pembeli, nama, kontak)