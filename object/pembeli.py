class Pembeli:
    def __init__(self, id_pembeli, nama, kontak):
        self.nama = nama
        self.kontak = kontak
    
    def __str__(self):
        return f"{self.nama} ({self.kontak})"
    