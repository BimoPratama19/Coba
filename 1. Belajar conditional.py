# ====================================================================================================
# BELAJAR PERCABANGAN (IF, ELIF, ELSE)
# ====================================================================================================



# ====================================================================================================
# CHEATSET PERCABANGAN
# ====================================================================================================

# Sintaks

# if kondisi_1:
#     ...                 # jalan jika kondisi_1 True
# elif kondisi_2:
#     ...                 # jalan jika kondisi_1 False dan kondisi_2 True
# else:
#     ...                 # jalan jika semua di atas False


# Aturan	                Keterangan
# Titik dua :	            Wajib di akhir if, elif, else
# Indentasi	                4 spasi, konsisten dalam satu blok
# elif	                    Boleh 0 atau lebih
# else	                    Boleh 0 atau 1, harus di paling akhir, tanpa kondisi
# Eksekusi	                Dicek dari atas, berhenti di True pertama

# Operator
# Kategori	                Operator
# Perbandingan	            == != > < >= <=
# Logika	                and or not
# Keanggotaan	            in not in
# Rentang	                a <= x <= b

# Tabel Kebenaran
# A	        B	        A and B	     A or B	    not A
# True	    True	    True	     True	    False
# True	    False	    False	     True	    False
# False	    True	    False	     True	    True
# False	    False	    False	     False	    True

# Prioritas: not → and → or (pakai kurung bila ragu)


# Falsy vs Truthy
# Falsy	                                Truthy
# False, 0, 0.0, "", [], None	        selain itu (5, -1, "a", " ", [0])


# Pola Cepat
# Kebutuhan	                        Kode
# Genap	                            x % 2 == 0
# Kelipatan n	                    x % n == 0
# Dalam rentang	                    a <= x <= b
# Vokal	                            c.lower() in "aiueo"
# Input tidak peduli kapital	    s.lower() == "ya"
# Salah satu dari beberapa nilai	x in (1, 2, 3)
# Batas bawah	                    if x < 0: x = 0
# Ternary	                        a if kondisi else b


# Checklist Debug
#  Ada : di akhir baris if/elif/else?
#  Indentasi konsisten?
#  Pakai ==, bukan =?
#  Hasil input() sudah di-int() atau float()?
#  Urutan elif dari yang paling ketat ke yang paling longgar?
#  or ditulis lengkap (x == 1 or x == 2)?
#  Batas inklusif/eksklusif (> vs >=) sudah sesuai soal?

# ====================================================================================================
# DRILING SOAL
# ====================================================================================================

# -----------------------------------
#               EASY
# -----------------------------------

# SOAL 1 (Warung Kopi Lereng Senja: Rekomendasi Minuman)

# print("=== WARUNG KOPI LERENG SENJA ===")

# suhu = int(input("Masukkan suhu udara (Celsius): "))
# hujan = input("Apakah sedang hujan? (ya/tidak): ").lower()
# jumlah_gelas = int(input("Masukkan jumlah gelas: "))


# if hujan == "ya":
#     if suhu < 20:
#         menu = "Cokelat Panas"
#         harga = 18000
#     else:
#         menu = "Teh Jahe"
#         harga = 12000

# else:
#     if suhu >= 30:
#         menu = "Es Kopi Susu"
#         harga = 20000
#     elif 20 <= suhu < 30:
#         menu = "Kopi Susu Hangat"
#         harga = 16000
#     else:
#         menu = "Wedang Ronde"
#         harga = 14000


# if jumlah_gelas >= 5:
#     diskon = 5000
# else:
#     diskon = 0

# subtotal = harga * jumlah_gelas
# total_bayar = subtotal - diskon

# print("================================")
# print(f"Rekomendasi: {menu}")
# print(f"Harga per gelas: Rp{harga}")
# print(f"Subtotal: Rp{subtotal}")
# print(f"Diskon: Rp{diskon}")
# print(f"Total bayar: Rp{total_bayar}")
# print("================================")

# ====================================================================================================

# SOAL 2 (Taman Kupu-Kupu Pelangi)

# print("=== TAMAN KUPU-KUPU PELANGI ===")

# umur = int(input("Masukkan umur pengunjung: "))
# hari_libur = input("Apakah hari libur? (ya/tidak): ").lower()
# bawa_kamera = input("Apakah membawa kamera? (ya/tidak): ").lower()

# if umur < 5:
#     kategori = "Balita"
#     harga_tiket = 0

# elif 5 <= umur <= 12:
#     kategori = "Anak"
#     harga_tiket = 15000

# elif 13 <= umur <= 59:
#     kategori = "Dewasa"
#     harga_tiket = 30000

# else:
#     kategori = "Lansia"
#     harga_tiket = 20000

# # Biaya tambahan
# biaya_hari_libur = 0
# biaya_kamera = 0
# if hari_libur == "ya":
#     if kategori == "Balita":
#         biaya_hari_libur += 0
#     else:
#         biaya_hari_libur += 5000

# if bawa_kamera == "ya":
#     biaya_kamera += 10000

# total_bayar = harga_tiket + biaya_hari_libur + biaya_kamera

# print("================================")
# print(f"Kategori: {kategori}")
# print(f"Tiket dasar: Rp{harga_tiket}")
# print(f"Biaya hari libur: Rp{biaya_hari_libur}")
# print(f"Biaya kamera: Rp{biaya_kamera}")
# print(f"Total bayar: Rp{total_bayar}")
# print("================================")

# ====================================================================================================

# SOAL 3 ()








# -----------------------------------
#              MEDIUM
# -----------------------------------

# SOAL 1 (Penyewaan Kapal Wisata Pulau Karang)

# print("=== PELABUHAN PULAU KARANG ===")

# jenis_kapal = input("Masukkan jenis kapal (speedboat/perahu/kano): ").lower()
# jumlah_penumpang = int(input("Masukkan jumlah penumpang: "))
# durasi_sewa = int(input("Masukkan durasi sewa (jam): "))
# punya_member = input("Apakah memiliki kartu member? (ya/tidak): ").lower()
# metode_bayar = input("Masukkan metode pembayaran (tunai/dompet): ").lower()
# if metode_bayar == "dompet":
#     saldo_dompet = int(input("Masukkan saldo dompet: "))

# # Tarif sewa per jam
# if jenis_kapal == "speedboat":
#     tarif_perjam = 100000
# elif jenis_kapal == "perahu":
#     tarif_perjam = 60000
# else:
#     tarif_perjam = 25000

# # Sewa dasar
# sewa_dasar = tarif_perjam * durasi_sewa

# # Presentase diskon
# diskon_durasi = 0
# if durasi_sewa >= 6:
#     diskon_durasi = 20
# elif 3 <= durasi_sewa <= 5:
#     diskon_durasi = 10

# diskon_member = 0
# if punya_member == "ya":
#     diskon_member = 5

# diskon_total = diskon_durasi + diskon_member
# if diskon_total > 20:
#     diskon_total = 20

# nominal_diskon = (sewa_dasar * diskon_total) // 100

# # Biaya penumpang tambahan
# biaya_tambahan = 0
# if jumlah_penumpang > 4:
#     biaya_tambahan += (jumlah_penumpang - 4)*10000

# total_bayar = sewa_dasar - nominal_diskon + biaya_tambahan

# print("================================")
# print(f"Sewa dasar: Rp{sewa_dasar}")
# print(f"Diskon ({diskon_total}%): Rp{nominal_diskon}")
# print(f"Biaya penumpang tambahan: Rp{biaya_tambahan}")
# print(f"Total bayar: Rp{total_bayar}")
# print("================================")
# if metode_bayar == "dompet":
#     if saldo_dompet >= total_bayar:
#         print(f"Sisa saldo: Rp{saldo_dompet - total_bayar}")
#     else:
#         print("Saldo tidak mencukupi.")
#         print(f"Kekurangan saldo: Rp{total_bayar - saldo_dompet}")

# else:
#     print("Pembayaran dilakukan secara tunai.")

# print("================================")

# ====================================================================================================


# SOAL 2 (Ekspedisi Awan Kirim)

print("=== EKSPEDISI AWAN KIRIM ===")
layanan = input("Masukkan layanan (reguler/ekspres/kargo): ").lower()
berat_paket = int(input("Masukkan berat paket (kg): "))
zona = int(input("Masukkan zona tujuan (1/2/3): "))
pakai_asuransi = input("Apakah memakai asuransi? (ya/tidak): ").lower()
kode_promo = input("Masukkan kode promo (hemat/gratis/tidak): ").lower()
metode_bayar = input("Masukkan metode pembayaran (transfer/cod): ").lower()
if metode_bayar == "transfer":
    saldo_rekening = int(input("Masukkan saldo rekening: "))

# 1 dan 2
berat_ditagih = berat_paket
if layanan == "reguler":
    tarif = 8000
elif layanan == "ekspres":
    tarif = 15000
elif layanan == "kargo":
    tarif = 5000
    if berat_paket < 10:
        berat_ditagih = 10

# 3
biaya_dasar = tarif * berat_ditagih
if zona == 1:
    faktor_zona = 100
elif zona == 2:
    faktor_zona = 120
else:
    faktor_zona = 150
ongkir = biaya_dasar * faktor_zona // 100

# 4
if pakai_asuransi == "ya":
    asuransi = ongkir * 2 // 100
    if asuransi < 3000:
        asuransi = 3000
else:
    asuransi = 0

# 5
if kode_promo == "hemat":
    diskon = ongkir * 10 // 100
elif kode_promo == "gratis":
    diskon = 15000
    if ongkir < 15000:
        diskon = ongkir
else:
    diskon = 0

# 6 dan 7
total_bayar = ongkir - diskon + asuransi
if metode_bayar == "cod":
    status = "Bayar di tempat saat paket diterima."
else:
    if saldo_rekening >= total_bayar:
        status = f"Sisa saldo: Rp{saldo_rekening - total_bayar}"
    else:
        status = f"Saldo tidak mencukupi.\nKekurangan saldo: Rp{total_bayar - saldo_rekening}"

print("================================")
print(f"Layanan: {layanan}")
print(f"Berat ditagih: {berat_ditagih} kg")
print(f"Ongkir: Rp{ongkir}")
print(f"Asuransi: Rp{asuransi}")
print(f"Diskon: Rp{diskon}")
print(f"Total bayar: Rp{total_bayar}")
print("================================")
print(status)
print("================================")






# -----------------------------------
#              HARD
# -----------------------------------

