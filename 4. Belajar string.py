# ====================================================================================================
# BELAJAR STRING
# ====================================================================================================



# ====================================================================================================
# CHEATSET STRING
# ====================================================================================================

# Dasar
# Topik	                    Sintaks	                        Contoh → Hasil
# Buat string	            '..', "..", """..."""	        "hai"
# Panjang	                len(s)	                        len("hai") → 3
# Gabung	                a + b	                        "a" + "b" → "ab"
# Ulang	                    s * n	                        "ab" * 2 → "abab"
# Cek isi	                x in s / x not in s	            "a" in "kata" → True
# Ke string	                str(x)	                        str(5) → "5"

# Indexing dan slicing (s = "PYTHON")
# Ekspresi	                Hasil	                    Keterangan
# s[0] / s[-1]	            P / N	                    pertama / terakhir
# s[1:4]	                YTH	                        stop tidak ikut
# s[:3] / s[3:]	            PYT / HON	                dari awal / sampai akhir
# s[-3:]	                HON	                        3 karakter terakhir
# s[::2]	                PTO	                        loncat 2
# s[::-1]	                NOHTYP	                    dibalik

# Method penting
# Kelompok	        Method	                                Fungsi
# Huruf	            upper() lower() capitalize() 
#                   title() swapcase()	                    ubah besar/kecil

# Spasi	            strip() lstrip() rstrip()	            hapus spasi/karakter di tepi
# Cari	            find(x) rfind(x) 
#                   index(x) count(x)	                    posisi / jumlah; find → -1 jika tidak ada
# Awal/akhir	    startswith(x) endswith(x)	            hasil True/False
# Ganti	            replace(lama, baru, n)	                n opsional
# Pecah/gabung	    split(sep) sep.join(list)	            string ↔ list
# Cek jenis	        isalpha() isdigit() isalnum() 
#                   isspace() islower() isupper()	        hasil True/False
# Rata	            center(w, c) ljust(w, c)    
#                   rjust(w, c) zfill(w)	                lebar w, isi karakter c

# Formatting
# Tujuan	                    Sintaks	                            Hasil
# Sisip variabel	            f"{x}"	                            nilai x
# 2 desimal	                    f"{x:.2f}"	                        3.14
# Ribuan	                    f"{x:,}"	                        1,234,567
# Persen	                    f"{x:.1%}"	                        25.6%
# Isi nol	                    f"{x:03d}"	                        007
# Rata kiri/kanan/tengah	    f"{x:<8}" f"{x:>8}" f"{x:^8}"	    lebar 8

# Escape dan karakter
# Kode	        Arti	        Kode	                Arti
# \n	        baris baru	    \\	                    backslash
# \t	        tab	            \' \"	                kutip
# r"..."	    raw string	    ord(c) / chr(n)	        karakter ↔ kode

# ====================================================================================================
# DRILING SOAL
# ====================================================================================================

# -----------------------------------
#               EASY
# -----------------------------------

# SOAL 1 (Mesin Label Gudang Ekspedisi)

# # Meminta input user
# nama_penerima = input("Masukkan nama penerima: ")
# kota_tujuan = input("Masukkan kota tujuan: ")
# nomor_resi = input("Masukkan nomor resi: ")

# # pengolahan input
# nama_label = nama_penerima.upper()
# panjang_nama = len(nama_penerima)
# list_nama = nama_label.split()
# inisial = list_nama[0][0] + list_nama[1][0]
# kode_kota = kota_tujuan[:3].upper()
# resi_bersih = nomor_resi.replace("-","")
# kode_label = f"{kode_kota}-{inisial}-{resi_bersih[-4:]}"

# # cetak output
# print("============================")
# print("|| LABEL PAKET KILATKIRIM ||")
# print("============================")
# print(f"Penerima     : {nama_label}")
# print(f"Inisial      : {inisial}")
# print(f"Panjang nama : {panjang_nama} karakter")
# print(f"Kode kota    : {kode_kota}")
# print(f"Nomor resi   : {resi_bersih}")
# print(f"Kode label   : {kode_label}")
# print("============================")

# ====================================================================================================

# SOAL 2 (Kurator Kutipan Perpustakaan Kota)

# print("=== KURATOR KUTIPAN ===")
# # Meinta input user
# kutipan = input("Masukkan kutipan: ")
# kata_cari = input("Masukkan kata yang dicari: ")
# kata_pengganti = input("Masukkan kata pengganti: ")
# # pengolahan input
# kutipan_bersih = kutipan.strip()
# judul_kutipan = kutipan_bersih.title()
# panjang_kutipan = len(kutipan_bersih)
# jumlah_kata = len(kutipan_bersih.split())
# posisi_kata = kutipan_bersih.find(kata_cari)
# jumlah_muncul = kutipan_bersih.count(kata_cari)
# kutipan_baru = kutipan_bersih.replace(kata_cari, kata_pengganti)
# # Tampilkan output
# print("-----------------------")
# print(f"Kutipan bersih: {kutipan_bersih}")
# print(f"Judul kutipan: {judul_kutipan}")
# print(f"Panjang kutipan: {panjang_kutipan} karakter")
# print(f"Jumlah kata: {jumlah_kata}")
# print(f"Posisi kata cari: {posisi_kata}")
# print(f"Kemunculan kata cari: {jumlah_muncul}")
# print(f"Kutipan baru: {kutipan_baru}")
# print("=======================")

# ====================================================================================================

# SOAL 3 (Pendaftaran Guild Petualang Lumina)

# Meminta input user
nama_karakter = input("Masukkan nama karakter: ")
kelas_karakter = input("Masukkan kelas karakter: ")
nomor_urut = int(input("Masukkan nomor urut pendaftaran: "))
tanggal_daftar = input("Masukkan tanggal daftar (DD-MM-YYYY): ")

# Mengolah input
nama_tampil = nama_karakter.capitalize()
julukan = nama_karakter[::-1].capitalize()
kelas_besar = kelas_karakter.upper()
nomor_id = str(nomor_urut).zfill(3)
bulan = tanggal_daftar[3:5]
tahun = tanggal_daftar[6:10]
kode_guild = kelas_besar[:2] + "-" + nomor_id + "-" + bulan + tahun[-2:]

# Menampilkan output
print("==============================")
print("|| PENDAFTARAN GUILD LUMINA ||")
print("==============================")
print(f"Nama karakter : {nama_tampil}")
print(f"Nama julukan  : {julukan}")
print(f"Kelas         : {kelas_besar}")
print(f"Nomor ID      : {nomor_id}")
print(f"Bulan daftar  : {bulan}")
print(f"Tahun daftar  : {tahun}")
print(f"Kode guild    : {kode_guild}")
print("==============================")

# ====================================================================================================

# -----------------------------------
#              MEDIUM
# -----------------------------------











# ====================================================================================================

# -----------------------------------
#              HARD
# -----------------------------------

# ====================================================================================================