def cari_denda_terbesar(daftar_denda):
    denda_terbesar = 0
    nomor_buku = 1
    for nomor, denda in enumerate(daftar_denda, start=1):
        if denda > denda_terbesar:
            denda_terbesar = denda
            nomor_buku = nomor
    return denda_terbesar, nomor_buku
print(cari_denda_terbesar([-5, -2, -9]))