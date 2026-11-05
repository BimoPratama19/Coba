# ====================================================================================================
# BELAJAR TUPLE
# ====================================================================================================



# ====================================================================================================
# CHEATSET TUPLE
# ====================================================================================================

# Membuat
# Tujuan	                    Sintaks	                    Hasil
# Tuple kosong	                () atau tuple()	            ()
# Tuple biasa	                (1, 2, 3)	                (1, 2, 3)
# Tanpa kurung	                1, 2, 3	                    (1, 2, 3)
# 1 elemen	                    (5,)	                    (5,)
# Dari iterable	                tuple("abc")	            ('a', 'b', 'c')

# Akses
# Tujuan	                    Sintaks
# Elemen ke-i	                t[i]
# Elemen terakhir	            t[-1]
# Slicing	                    t[start:stop:step]
# Dibalik	                    t[::-1]
# Jumlah elemen	                len(t)

# Operasi dan Fungsi
# Tujuan	                    Sintaks
# Gabung	                    t1 + t2
# Ulang	                        t * n
# Cek isi	                    x in t, x not in t
# Hitung kemunculan	            t.count(x)
# Cari index pertama	        t.index(x) (error jika tidak ada)
# Min / Max / Jumlah	        min(t), max(t), sum(t)
# Urutkan (hasil list)	        sorted(t), sorted(t, reverse=True)

# Iterasi dan Unpacking
# Tujuan	                    Sintaks
# Loop elemen	                for x in t:
# Loop index + elemen	        for i, x in enumerate(t, start=1):
# Loop dua tuple	            for a, b in zip(t1, t2):
# Unpacking                 	a, b, c = t
# Star unpacking	            first, *mid, last = t (mid berupa list)
# Swap	                        a, b = b, a
# Abaikan nilai	                _, y = t

# ====================================================================================================
# DRILING SOAL
# ====================================================================================================

# -----------------------------------
#               EASY
# -----------------------------------

# SOAL 1 (Stasiun Cuaca Puncak Gunung)

# print("=== STASIUN CUACA PUNCAK ===")

# data_suhu = ()
# for i in range(1, 8):
#     suhu = int(input(f"Masukkan suhu hari ke-{i}: "))
#     data_suhu += (suhu,)    

# print(f"Data suhu: {data_suhu}")
# print(f"Suhu terendah: {min(data_suhu)}")
# print(f"Suhu tertinggi: {max(data_suhu)}")
# print(f"Selisih: {max(data_suhu) - min(data_suhu)}")
# print(f"Rata-rata: {sum(data_suhu)/len(data_suhu):.2f}")

# diatas_ratarata = 0
# for suhu in data_suhu:
#     if suhu > (sum(data_suhu)/len(data_suhu)):
#         diatas_ratarata += 1
# print(f"Hari di atas rata-rata: {diatas_ratarata}")
# print(f"Hari pertama suhu tertinggi: {data_suhu.index(max(data_suhu)) + 1}")

# ====================================================================================================

# -----------------------------------
#              MEDIUM
# -----------------------------------

# SOAL 1 ()

print("=== EKSPEDISI KILAT ===")
KOTA = (("Bandung", 9000), ("Surabaya", 12000), ("Medan", 20000), ("Makassar", 25000))

banyak_paket = int(input("Masukkan jumlah paket: "))

# Menampung data
rekap_paket = ()
jumlah_paket_kota = (0, 0, 0, 0)
total_berat_kota = (0, 0, 0, 0)

# Loop sebanyak "banyak paket"
for i in range(banyak_paket):
    nomor_kota = int(input(f"Masukkan nomor kota tujuan paket ke-{i+1} (1-4): "))
    berat_kg = int(input(f"Masukkan berat paket ke-{i+1} (kg): "))

    indeks_kota = nomor_kota - 1   
    nama_kota, tarif_kota = KOTA[indeks_kota]
    if berat_kg > 10:
        biaya_tambahan = 5000
    else:
        biaya_tambahan = 0
    biaya_dasar = tarif_kota * berat_kg
    biaya = biaya_dasar + biaya_tambahan

    rekap_paket += ((nama_kota, berat_kg, biaya),)
    jumlah_paket_kota = (jumlah_paket_kota[:indeks_kota] + (jumlah_paket_kota[indeks_kota] + 1,) + jumlah_paket_kota[indeks_kota+1:])
    total_berat_kota = (total_berat_kota[:indeks_kota] + (total_berat_kota[indeks_kota] + berat_kg,) + total_berat_kota[indeks_kota + 1:])


print("--- Rincian Paket ---")

# Mencetak rincian paket dan menentukan termahal, terberat dan lain lain
total_biaya = 0
kota_termahal, paket_terberat, biaya_termahal = rekap_paket[0] 

for nomor, (nama_kota, berat_kg, biaya) in enumerate(rekap_paket, start=1):
    print(f"{nomor}. {nama_kota} {berat_kg}kg = Rp{biaya}")
    total_biaya += biaya
    if biaya > biaya_termahal:
        biaya_termahal = biaya
        kota_termahal = nama_kota

kota_terbanyak = jumlah_paket_kota[0]
kota_terberat = total_berat_kota[0]
nama_kota_terberat = KOTA[0][0]
nama_kota_terbanyak = KOTA[0][0]
nama_kota_tanpa_paket = ""

for i in range(len(total_berat_kota)):
    if total_berat_kota[i] > kota_terberat:
        kota_terberat = total_berat_kota[i]
        nama_kota_terberat = KOTA[i][0]
    if jumlah_paket_kota[i] > kota_terbanyak:
        kota_terbanyak = jumlah_paket_kota[i]
        nama_kota_terbanyak = KOTA[i][0]

    if jumlah_paket_kota[i] == 0:
        if nama_kota_tanpa_paket != "":
            nama_kota_tanpa_paket += ", "
        nama_kota_tanpa_paket += KOTA[i][0]

if nama_kota_tanpa_paket == "":
    nama_kota_tanpa_paket = "-"

print("--- Ringkasan ---")
print(f"Total biaya: Rp{total_biaya}")
print(f"Paket termahal: {kota_termahal} (Rp{biaya_termahal})")
print(f"Kota terbanyak paket: {nama_kota_terbanyak} ({kota_terbanyak} paket)")
print(f"Kota terberat paket: {nama_kota_terberat} ({kota_terberat} kg)")
print(f"Kota tanpa paket: {nama_kota_tanpa_paket}")






# ====================================================================================================

# -----------------------------------
#              HARD
# -----------------------------------