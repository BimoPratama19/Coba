


















# print("=== BUKU HARTA KAPTEN ===")

# jumlah_catatan =  int(input("Masukkan jumlah catatan harta: "))

# daftar_harta = {}
# for i in range(1, jumlah_catatan + 1):
#     nama_harta = input(f"Masukkan nama harta ke-{i}: ").title()
#     jumlah_harta = int(input(f"Masukkan jumlah harta ke-{i}: "))
#     if nama_harta in daftar_harta:
#         daftar_harta[nama_harta] += jumlah_harta
#     else:
#         daftar_harta[nama_harta] = jumlah_harta
        

# harta_dicari = input("Masukkan harta yang dicari: ").title()
# jumlah_dicari = 0
# total_jenis_harta = len(daftar_harta)
# total_harta_keseluruhan = 0

# print("--- Rekap Harta ---")
# for harta, jumlah in daftar_harta.items():
#     print(f"{harta}: {jumlah}")
#     total_harta_keseluruhan += jumlah
#     if harta == harta_dicari:
#         jumlah_dicari += jumlah

# print("-------------------")
# print(f"Total jenis harta: {total_jenis_harta}")
# print(f"Total seluruh harta: {total_harta_keseluruhan}")
# if jumlah_dicari != 0:
#     print(f"Jumlah {harta_dicari}: {jumlah_dicari}")
# else:
#     print(f"{harta_dicari} tidak ditemukan di kapal")



with open("test.txt", "r", encoding="UTF-8") as f:
    hasil = []
    i = 1
    for baris in f:
        baris = baris.strip()
        if i % 2 == 0:
            hasil.append(baris)
        i += 1

    print(hasil)


