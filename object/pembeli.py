class Pembeli:
    def __init__(self, id_pembeli, nama, kontak):
        self.id_pembeli = id_pembeli
        self.nama = nama
        self.kontak = kontak
    
    def __str__(self):
        return f"{self.nama} ({self.kontak})"