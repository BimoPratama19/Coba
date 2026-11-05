# ====================================================================================================
# BELAJAR PERULANGAN
# ====================================================================================================



# ====================================================================================================
# CHEATSET PERULANGAN
# ====================================================================================================

# Kebutuhan	                            Kode
# Ulang N kali	                        for i in range(N):
# Angka a sampai b (b ikut)	            for i in range(a, b + 1):
# Loncat step	                        for i in range(a, b, step):
# Hitung mundur	                        for i in range(n, 0, -1):
# Per karakter string	                for c in teks:
# Per elemen list	                    for item in daftar:
# Indeks + elemen	                    for i, item in enumerate(daftar):
# Ulang sampai kondisi salah	        while kondisi:
# Loop tak hingga terkontrol	        while True: + break

# Kontrol
# Kata kunci	                        Fungsi
# break	                                Keluar dari loop terdekat
# continue	                            Lompat ke iterasi berikutnya
# else (pada loop)	                    Jalan jika loop selesai tanpa break
# _	                                    Nama variabel loop yang tidak dipakai


# Akumulator
# total = 0                      # perkalian: mulai dari 1
# for x in data:
#     total += x

# # Counter
# jumlah = 0
# for x in data:
#     if kondisi:
#         jumlah += 1

# # Terbesar / terkecil
# terbesar = data[0]
# for x in data:
#     if x > terbesar:
#         terbesar = x

# # Bangun string (belakang / depan)
# hasil = ""
# for c in teks:
#     hasil += c                 # urutan sama
#     # hasil = c + hasil        # urutan terbalik

# # Bandingkan dengan sebelumnya
# sebelumnya = ""
# for c in teks:
#     if c != sebelumnya:
#         ...                    # karakter berbeda dari sebelumnya
#     sebelumnya = c             # SELALU update di akhir iterasi

# # Sentinel
# x = input("...")
# while x != "STOP":
#     ...                        # proses x
#     x = input("...")           # input ulang di dalam loop



# ====================================================================================================
# DRILING SOAL
# ====================================================================================================

# -----------------------------------
#               EASY
# -----------------------------------

# SOAL 1 (Observatorium Bintang)

# print("=== OBSERVATORIUM BINTANG ===")
# jumlah_bintang = int(input("Masukkan jumlah bintang: "))

# total_kecerahan = 0
# bintang_terang = 0
# for i in range(1, jumlah_bintang + 1):
#     kecerahan = int(input(f"Masukkan kecerahan bintang ke-{i}: "))
#     if kecerahan >= 70:
#         bintang_terang += 1
#     total_kecerahan += kecerahan
    
# rata_rata = total_kecerahan/jumlah_bintang
# print("--- Hasil Pencatatan ---")
# print(f"Jumlah bintang terang: {bintang_terang}")
# print(f"Total kecerahan: {total_kecerahan}")
# print(f"Rata-rata kecerahan: {rata_rata:.1f}")

# ====================================================================================================

# SOAL 2 (Menara Harta Karun)

# print("=== MENARA HARTA KARUN ===")
# koin = int(input("Masukkan koin dalam peti (-1 untuk selesai): "))

# jumlah_peti_dibuka = 0
# total_koin = 0
# koin_terbanyak = koin
# jumlah_peti_kosong = 0  
# while koin != -1:
#     jumlah_peti_dibuka += 1
#     total_koin += koin
#     if koin > koin_terbanyak:
#         koin_terbanyak = koin
#     if koin == 0:
#         jumlah_peti_kosong += 1
#     koin = int(input("Masukkan koin dalam peti (-1 untuk selesai): "))
    
    
# print("--- Laporan Petualang ---")
# print(f"Jumlah peti dibuka: {jumlah_peti_dibuka}")
# print(f"Total koin: {total_koin}")
# print(f"Koin terbanyak dalam satu peti: {koin_terbanyak}")
# print(f"Jumlah peti kosong: {jumlah_peti_kosong}")

# ====================================================================================================

# SOAL 3 (Detektif Kata Sandi)

# print("=== PEMERIKSA KEKUATAN KATA SANDI ===")
# kata_sandi = input("Masukkan kata sandi: ")
# print("--- Hasil Analisis ---")

# huruf_kecil = 0
# huruf_besar = 0
# angka = 0
# simbol = 0
# for i in range(len(kata_sandi)):
#     if kata_sandi[i].islower():
#         huruf_kecil += 1
#     elif kata_sandi[i].isupper():
#         huruf_besar += 1
#     elif kata_sandi[i].isdigit():
#         angka += 1
#     else:
#         simbol += 1
    
# panjang = huruf_kecil + huruf_besar + angka + simbol
# if huruf_besar < 1 or huruf_kecil < 1 or angka < 1 or panjang < 8:
#     status = "LEMAH"
# else:
#     status = "KUAT"

# print(f"Panjang: {panjang}")
# print(f"Huruf besar: {huruf_besar}")
# print(f"Huruf kecil: {huruf_kecil}")
# print(f"Angka: {angka}")
# print(f"Simbol: {simbol}")
# print(f"Kekuatan: {status}")

# -----------------------------------
#              MEDIUM
# -----------------------------------

# SOAL 1 (Pencatat Pengeluaran Bulanan)
# print("=== PENCATAT PENGELUARAN ===")

# anggaran = int(input("Masukkan anggaran bulanan (rupiah): "))
# total_pengeluaran = 0
# total_makan = 0
# total_transport = 0
# total_hiburan = 0
# total_lainnya = 0

# terboros = 0
# kategori_terboros = ""
# jumlah_diterima = 0
# jumlah_ditolak = 0
# peringatan = False

# while True:
#     kategori = input("Masukkan kategori (SELESAI untuk berhenti): ").upper()
#     if kategori == "SELESAI":
#         break
#     if kategori not in ["SELESAI", "MAKAN", "HIBURAN", "TRANSPORT"]:
#         kategori = "LAINNYA"
#     nominal = int(input("Masukkan nominal (rupiah): "))

#     if total_pengeluaran + nominal > anggaran:
#         print(f"Transaksi ditolak: melebihi anggaran")
#         jumlah_ditolak += 1
#     else:
#         print(f"Transaksi diterima: {kategori} Rp{nominal}")
#         jumlah_diterima += 1
#         total_pengeluaran += nominal
#         if kategori == "MAKAN":
#             total_makan += nominal
#             if total_makan > terboros:
#                 terboros = total_makan
#                 kategori_terboros = kategori

#         elif kategori == "TRANSPORT":
#             total_transport += nominal
#             if total_transport > terboros:
#                 terboros = total_transport
#                 kategori_terboros = kategori

#         elif kategori == "HIBURAN":
#             total_hiburan += nominal
#             if total_hiburan > terboros:
#                 terboros = total_hiburan
#                 kategori_terboros = kategori
#         else:
#             total_lainnya += nominal
#             if total_lainnya > terboros:
#                 terboros = total_lainnya
#                 kategori_terboros = kategori
        
#         if total_pengeluaran * 100 >= anggaran * 80 and peringatan == False:
#             print(f"PERINGATAN: Pengeluaran sudah mencapai 80% anggaran!")
#             peringatan = True


# print("=== REKAP PENGELUARAN ===")
# print(f"MAKAN: Rp{total_makan}")
# print(f"TRANSPORT: Rp{total_transport}")
# print(f"HIBURAN: Rp{total_hiburan}")
# print(f"LAINNYA: Rp{total_lainnya}")
# print("-------------------------")
# print(f"Total pengeluaran: Rp{total_pengeluaran}")
# print(f"Sisa anggaran: Rp{anggaran - total_pengeluaran}")
# print(f"Transaksi diterima: {jumlah_diterima}")
# print(f"Transaksi ditolak: {jumlah_ditolak}")
# print(f"Kategori terboros: {kategori_terboros}")

# ====================================================================================================

# SOAL 2 (Robot Pembersih Lantai)

print("=== ROBOT PEMBERSIH LANTAI ===")

perintah = input("Masukkan rangkaian perintah: ").upper()

arah = 0    #0 = Utara, 1 = Timur, 2 = Selatan, 3 = Barat
langkah_berhasil = 0
tabrakan = 0
perintah_takdikenal = 0

# koordinat calon posisi
x = 0
y = 0
for i in perintah:
    if i == "M":
        if arah == 0:
            y += 1
        elif arah == 2:
            y -= 1
        elif arah == 1:
            x += 1
        elif arah == 3:
            x -= 1

        if x < -3 or x > 3 or y < -3 or y > 3:
            tabrakan += 1
            if arah == 0:
                y -= 1
            elif arah == 2:
                y += 1
            elif arah == 1:
                x -= 1
            else:
                x += 1
        else:
            langkah_berhasil += 1


    elif i == "L":
        arah = (arah - 1)%4

    elif i == "R":
        arah = (arah + 1)%4

    else:
        perintah_takdikenal += 1

    if tabrakan >= 3:
        break

#0 = Utara, 1 = Timur, 2 = Selatan, 3 = Barat
if arah == 0:
    arah_akhir = "Utara"
elif arah == 1:
    arah_akhir = "Timur"
elif arah == 2:
    arah_akhir = "Selatan"
else:
    arah_akhir = "Barat"

if tabrakan < 3:
    status = "Robot menjalankan semua perintah"
else:
    status = "Robot berhenti: 3 kali menabrak dinding"


posisi_akhir = (x, y)
jarak_dari_titik_awal = abs(x) + abs(y)

print("--- Laporan Robot ---")
print(f"Posisi akhir: {posisi_akhir}")
print(f"Arah akhir: {arah_akhir}")
print(f"Langkah berhasil: {langkah_berhasil}")
print(f"Tabrakan: {tabrakan}")
print(f"Perintah tidak dikenal: {perintah_takdikenal}")
print(f"Jarak dari titik awal: {jarak_dari_titik_awal}")
print(f"Status: {status}")


# -----------------------------------
#              HARD
# -----------------------------------



