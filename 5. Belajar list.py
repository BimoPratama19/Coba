# ====================================================================================================
# BELAJAR LIST
# ====================================================================================================



# ====================================================================================================
# CHEATSET LIST
# ====================================================================================================

# Pembuatan dan akses
# Sintaks	                                            Hasil
# [], [1, 2], list("abc"), list(range(n))	            membuat list
# lst[i], lst[-1]	                                    akses elemen (mulai 0; negatif dari belakang)
# lst[a:b], lst[a:b:s], lst[::-1]	                    slicing (b tidak ikut), hasil list baru
# lst[i] = x, lst[a:b] = [...]	                        ubah elemen / sebagian
# len(lst)	                                            jumlah elemen

# Method penting
# Tujuan	                Method	                                        Mengembalikan
# Tambah di akhir	        append(x)	                                    None
# Sisip di index	        insert(i, x)	                                None
# Tambah banyak	            extend(iter) atau lst + lst2	                None / list baru
# Hapus berdasar nilai	    remove(x)	                                    None
# Hapus berdasar index	    pop(i) (default terakhir), del lst[i]	        elemen / -
# Kosongkan	                clear()	                                        None
# Posisi nilai	            index(x)	                                    int
# Hitung kemunculan	        count(x)	                                    int
# Urut in-place	            sort(reverse=False, key=None)	                None
# Urut list baru	        sorted(lst)	                                    list baru
# Balik in-place	        reverse()	                                    None
# Salin	                    copy(), lst[:], list(lst)	                    list baru

# Fungsi bawaan dan operator
# Sintaks	                            Fungsi
# sum(lst), min(lst), max(lst)	        jumlah, terkecil, terbesar
# x in lst, x not in lst	            cek keanggotaan
# lst1 + lst2, lst * n	                gabung, ulang
# lst1 == lst2	                        sama jika isi dan urutannya sama
# "sep".join(lst), str.split()	        list string ↔ string

# Iterasi

# for x in lst: ...                     # per elemen
# for i in range(len(lst)): ...         # per index
# for i, x in enumerate(lst, start=1):  # index + elemen
# for a, b in zip(lst1, lst2):          # dua list berdampingan
# while lst: ...                        # selama list tidak kosong
# [ekspresi for x in lst if kondisi]    # comprehension

# Ingat selalu
# List itu mutable; b = a tidak menyalin.
# Method pengubah (append, sort, dll.) mengembalikan None.
# Jangan menghapus/menambah elemen dari list yang sedang di-loop.
# Cek in sebelum remove/index; cek if lst: sebelum pop.
# Nested list: gunakan comprehension, bukan [[x]*n]*m.

# ====================================================================================================
# DRILING SOAL
# ====================================================================================================

# -----------------------------------
#               EASY
# -----------------------------------

# SOAL 1 (Pemantau Hujan Meteor)

# # Meminta input user
# n = int(input("Masukkan jumlah jam pengamatan: "))

# data_meteor = []    # menyimpan data meteor
# for i in range(1, n + 1):
#     jumlah_meteor = int(input(f"Masukkan jumlah meteor jam ke-{i}: "))
#     data_meteor.append(jumlah_meteor)

# # Pengolahan data meteor
# total_meteor = sum(data_meteor)
# rata_rata = total_meteor / len(data_meteor)
# puncak = 0
# jam_puncak = 0
# diatas_ratarata = 0
# for j in range(len(data_meteor)):
#     if data_meteor[j] > puncak:
#         puncak = data_meteor[j]
#         jam_puncak = j + 1 
#     if data_meteor[j] > rata_rata:
#         diatas_ratarata += 1

# # Menampilkan output
# print(f"Data meteor: {data_meteor}")
# print(f"Total meteor: {total_meteor}")
# print(f"Rata-rata: {rata_rata:.2f}")
# print(f"Jam puncak: ke-{jam_puncak} ({puncak} meteor)")
# print(f"Jam di atas rata-rata: {diatas_ratarata}")

# ====================================================================================================

# SOAL 2 (Pemantau Suhu Gudang Es Krim)

# Meminta input user
# n = int(input("Masukkan jumlah jam pencatatan: "))

# data_suhu = []  # Menyimpan data suhu
# for i in range(1,n+1):
#     suhu = int(input(f"Masukkan suhu jam ke-{i}: "))
#     data_suhu.append(suhu)
# batas_aman = int(input("Masukkan batas aman (C): "))

# lewat_batas_aman = 0
# for s in data_suhu:
#     if s > batas_aman:
#         lewat_batas_aman += 1
# # Menampilkan output
# print(f"Data suhu: {data_suhu}")
# print(f"Suhu tertinggi: {max(data_suhu)} C (jam ke-{data_suhu.index(max(data_suhu)) + 1})")
# print(f"Suhu terendah: {min(data_suhu)} C (jam ke-{data_suhu.index(min(data_suhu)) + 1})")
# print(f"Selisih suhu: {max(data_suhu) - min(data_suhu)} C")
# print(f"Jam melewati batas aman: {lewat_batas_aman}")

# ====================================================================================================

# SOAL 3 (Pendakian Gunung Awan)

# n = int(input("Masukkan jumlah pos: "))

# tertinggi = 0
# pos_tertinggi = 1
# daftar_ketinggian = []
# for i in range(1, n + 1):
#     ketinggian_pos = int(input(f"Masukkan ketinggian pos ke-{i} (m): "))
#     daftar_ketinggian.append(ketinggian_pos)
#     if ketinggian_pos > tertinggi:
#         tertinggi = ketinggian_pos
#         pos_tertinggi = i


# tanjakan = 0
# turunan = 0
# pos_setelah_turunan = []
# for j in range(1, len(daftar_ketinggian)):
#     if daftar_ketinggian[j] > daftar_ketinggian[j-1]:
#         tanjakan += daftar_ketinggian[j]-daftar_ketinggian[j-1]
#     elif daftar_ketinggian[j] < daftar_ketinggian[j-1]:
#         turunan += daftar_ketinggian[j-1] - daftar_ketinggian[j]
#         pos_setelah_turunan.append(j + 1)
   
# print(f"Ketinggian pos: {daftar_ketinggian}")
# print(f"Pos tertinggi: ke-{pos_tertinggi} ({tertinggi} m)")
# print(f"Total tanjakan: {tanjakan} m")
# print(f"Total turunan: {turunan} m")
# print(f"Pos setelah turunan: {pos_setelah_turunan}")

# ====================================================================================================

# -----------------------------------
#              MEDIUM
# -----------------------------------

# SOAL 1 (Keranjang Belanja Bulanan)

# n = int(input("Masukkan jumlah barang: "))

# daftar_nama_barang = []
# daftar_harga_barang = []
# for i in range(1, n + 1):
#     nama_barang = input(f"Masukkan nama barang ke-{i}: ")
#     harga_barang = int(input(f"Masukkan harga barang ke-{i} (Rp): "))
#     daftar_nama_barang.append(nama_barang)
#     daftar_harga_barang.append(harga_barang)
# budget = int(input("Masukkan budget (Rp): "))

# barang_dihapus = 0
# while sum(daftar_harga_barang) > budget:
#     total_harga = sum(daftar_harga_barang)
    
#     tertinggi = daftar_harga_barang[0]
#     posisi_tertinggi = 0

#     for j in range(len(daftar_harga_barang)):
#         if daftar_harga_barang[j] > tertinggi:
#             tertinggi = daftar_harga_barang[j]
#             posisi_tertinggi = j

#     print(f"Hapus: {daftar_nama_barang[posisi_tertinggi]} (Rp{tertinggi})")
#     daftar_harga_barang.pop(posisi_tertinggi)
#     daftar_nama_barang.pop(posisi_tertinggi)
#     barang_dihapus += 1

# print(f"Barang tersisa: {daftar_nama_barang}")
# print(f"Total belanja: Rp{sum(daftar_harga_barang)}")
# print(f"Sisa budget: Rp{budget-sum(daftar_harga_barang)}")
# print(f"Barang dihapus: {barang_dihapus}")

# ====================================================================================================











# ====================================================================================================

# -----------------------------------
#              HARD
# -----------------------------------

# ====================================================================================================






