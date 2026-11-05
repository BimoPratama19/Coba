# ====================================================================================================
# BELAJAR PERULANGAN UNTUK POLA
# ====================================================================================================



# ====================================================================================================
# CHEATSET PERULANGAN UNTUK POLA
# ====================================================================================================

# Alat Dasar

# Kebutuhan	                                        Kode
# Cetak tanpa pindah baris	                        print("*", end="")
# Pindah baris	                                    print()
# Nested loop	                                    loop luar = baris, loop dalam = kolom
# Baris 1..n	                                    for i in range(1, n+1)
# Baris n..1	                                    for i in range(n, 0, -1)
# Variabel tak terpakai	                            for _ in range(k)
# Huruf ke-k (A=0)	                                chr(65 + k)
# Angka → teks	                                    str(angka)

# Rumus Pola Umum (baris i, tinggi n)

# Pola	                                    Spasi	                    Simbol
# Persegi n×n	                            0	                        n
# Segitiga naik	                            0	                        i
# Segitiga turun (i dari n ke 1)	        0	                        i
# Segitiga rata kanan	                    n - i	                    i
# Piramida	                                n - i	                    2*i - 1
# Piramida terbalik (i dari n ke 1)	        n - i	2*i - 1
# Berlian	                                piramida baris 1..n, lalu terbalik dari n-1 ke 1

# Pola Berbasis Kondisi

# Pola	                                    Kondisi cetak simbol
# Persegi berongga	                        i==0 or i==n-1 or j==0 or j==n-1
# Segitiga berongga	                        j==1 or j==i or i==n
# Diagonal utama	                        i == j
# Diagonal kedua	                        i + j == n - 1
# Papan catur	                            (i + j) % 2 == 0

# Template Siap Pakai

# Template A: pola dengan loop dalam terpisah (spasi + simbol)
# for i in range(1, n + 1):
#     for _ in range(JUMLAH_SPASI):
#         print(" ", end="")
#     for _ in range(JUMLAH_SIMBOL):
#         print("*", end="")
#     print()

# # Template B: pola berdasarkan kondisi posisi (i, j)
# for i in range(n):
#     for j in range(n):
#         if KONDISI:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# # Template C: bangun string per baris (aman dari spasi di ujung)
# for i in range(n):
#     teks_baris = ""
#     for j in range(k):
#         teks_baris += ...
#     print(teks_baris)

# ====================================================================================================
# DRILING SOAL
# ====================================================================================================

# -----------------------------------
#               EASY
# -----------------------------------

# SOAL 1 (Tangga Menuju mercusuar)

# print("=== TANGGA MERCUSUAR ===")
# tinggi = int(input("Masukkan tinggi tangga: "))

# total_anak_tangga = 0
# total_balok = 0
# for i in range(1, tinggi + 1):
#     print("#" * i)
#     total_balok += i
#     total_anak_tangga += 1
# for j in range(tinggi - 1, 0, -1):
#     print("#" * j)
#     total_anak_tangga += 1
#     total_balok += j

# print("------------------------")
# print(f"Total anak tangga: {total_anak_tangga}")
# print(f"Total balok: {total_balok}")

# ====================================================================================================

# SOAL 2 (Menara Lampion Festival)

# print("=== MENARA LAMPION ===")
# tinggi = int(input("Masukkan tinggi menara: "))
# simbol = input("Masukkan simbol lampion: ")

# total_lampion = 0
# lebar_dasar = 2*tinggi - 1
# for i in range(1, tinggi + 1): 
#     for _ in range(tinggi - i): 
#         print(" ", end="")
#     for _ in range(2*i - 1): 
#         print(simbol, end="")
#         total_lampion += 1
#     print()

# print("----------------------")
# print(f"Total lampion: {total_lampion}")
# print(f"Lebar dasar: {lebar_dasar}")

# ====================================================================================================

# SOAL 3 (Menara sandi Kapal Selam)

# print("=== MENARA SANDI ===")

# jumlah_lapisan = int(input("Masukkan jumlah lapisan: "))
# huruf_terakhir = ""
# total_huruf = 0
# for i in range(jumlah_lapisan):
#     teks = ""
#     for j in range(jumlah_lapisan - i):
#         teks += chr(65 + j)
#         teks += "-"
#         total_huruf += 1
#         if chr(65 + j) > huruf_terakhir:
#             huruf_terakhir = chr(65 + j)
#     print(teks.strip("-"))

# print("--------------------")
# print(f"Total huruf: {total_huruf}")
# print(f"Huruf terakhir: {huruf_terakhir}")

# ====================================================================================================

# SOAL 4 (Denah Kios Pasar Malam)

# print("=== DENAH KIOS PASAR MALAM ===")

# jumlah_baris = int(input("Masukkan jumlah baris: "))

# counter = 1
# jumlah = 0
# for i in range(1, jumlah_baris+1):
#     teks = ""
#     for j in range(i):
#         teks += str(counter)
#         if len(teks) > 0:
#             teks += " | "
#         jumlah += counter
#         counter += 1
#     print(teks.strip(" | "))

# print("------------------------------")
# print(f"Nomor kios terakhir: {counter-1}")
# print(f"Jumlah seluruh nomor: {jumlah}")

# ====================================================================================================

# SOAL 5 (Menara Gelas Champagne)

# print("=== MENARA GELAS ===")
# # Meminta inpuut user
# tinggi_menara = int(input("Masukkan tinggi menara: "))

# # Menghitung total gelas & jumlah label
# total_gelas = 0
# jumlah_label = 0

# # Looping untuk pola
# for i in range(1, tinggi_menara + 1):
#     teks = ""
#     for _ in range(tinggi_menara-i):
#         print(" ", end="")
#     for j in range(i, 0, -1):
#         if j < i:
#             teks += " "
#         teks += str(j)
#         total_gelas += 1
#         jumlah_label += j
#     print(teks)

# # Menampilkan output
# print("--------------------")
# print(f"Total gelas: {total_gelas}")
# print(f"Jumlah label: {jumlah_label}")

# ====================================================================================================

# SOAL 6 (Pemburu Tornado, Mengejar Badai di Padang Oklahoma)

# print("=== PEMBURU TORNADO ===")
# # Meminta input user
# tinggi_corong = int(input("Masukkan tinggi corong: "))

# lebar_mulut_corong = 2*tinggi_corong - 1
# counter = 0

# # Loop untuk pola segitiga terbalik
# for i in range(1, tinggi_corong + 1):
#     for _ in range(i - 1):
#         print(" ", end="")
#     for j in range(2 * (tinggi_corong - i) + 1):
#         print("@", end="")
#         counter += 1
#     print()

# # Cetak output
# print("------------------------")
# print(f"Total titik angin: {counter}")
# print(f"Lebar mulut corong: {lebar_mulut_corong}")

# ====================================================================================================

# SOAL 7 (Gulungan Mantra Penyihir Es)

print("=== GULUNGAN MANTRA ===")
# Meminta input user
jumlah_baris = int(input("Masukkan jumlah baris gulungan: "))

total_mantra = 0
banyak_kekuatan = 0

# Membuat pola dan menghitungnya
for i in range(1, jumlah_baris + 1):
    teks = ""
    for j in range(1, i + 1):
        if j != i:      # jika bukan di ujung ditambahkan ", "
            teks += (str(i * j) + ", ")
        else:
            teks += str(i * j)
        total_mantra += 1
        banyak_kekuatan += (i * j)
    print(teks)

# Cetak output
print("--------------------------")  
print(f"Total mantra: {total_mantra}")
print(f"Total kekuatan: {banyak_kekuatan}")






# ====================================================================================================

# -----------------------------------
#              MEDIUM
# -----------------------------------

# SOAL 1 (Gerbang Kristal Penjaga Dimensi)

# print("=== PORTAL KRISTAL ===")

# radius = int(input("Masukkan radius kristal: "))
# simbol_tepi = input("Masukkan simbol tepi: ")
# simbol_inti = input("Masukkan simbol inti: ")

# energi_tepi = 0
# energi_inti = 0
# for i in range(1, radius + 1):
#     for _ in range(radius - i):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         if j == 0 or j == 2 * i - 2:
#             print(simbol_tepi, end="")
#             energi_tepi += 1
#         else:
#             print(simbol_inti, end="")
#             energi_inti += 1
#     print()

# for k in range(1, radius):  
#     for _ in range(k):
#         print(" ", end ="")
#     for l in range((2*radius-1) - 2*k):
#         if l == 0 or l == (2*radius-1) - 2*k - 1:
#             print(simbol_tepi, end="")
#             energi_tepi += 1
#         else:
#             print(simbol_inti, end= "")
#             energi_inti += 1
#     print()

# print("----------------------")
# print(f"Energi tepi: {energi_tepi}")
# print(f"Energi inti: {energi_inti}")







# ====================================================================================================

# -----------------------------------
#              HARD
# -----------------------------------

# ====================================================================================================