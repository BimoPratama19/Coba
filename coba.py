
# ganjil = []
# genap = []

# while True:
#     angka = input("Masukkan angka: ")
#     if angka == "STOP":
#         break
#     if int(angka) % 2 == 0:
#         genap.append(int(angka))
#     else:
#         ganjil.append(int(angka))


# sum_ganjil = sum(ganjil)
# if len(genap) < 1:
#     kali_genap = 0
# else:
#     kali_genap = 1
#     for i in genap:
#         kali_genap *= i

# print(f"Sum nilai ganjil: {sum_ganjil}")
# print(f"Perkalian nilai genap: {kali_genap}")


#================================================================

# def sum_product(lst):
#     sum_index_genap = 0
#     kali_index_ganjil = 1
#     if len(lst) < 2:
#         kali_index_ganjil = 0
#     for i in range(len(lst)):
#         if i % 2 == 0:
#             sum_index_genap += lst[i]
#         else:
#             kali_index_ganjil *= lst[i]

#     return (sum_index_genap, kali_index_ganjil)

# print(sum_product([14, 174, 195, 858, 201, 880]))
# print(sum_product([565]))
# print(sum_product([]))
# # print(sum_product([]))

#================================================================


# def unique_count(lst):
#     unik = ""
#     for i in lst:
#         if str(i) not in unik:
#             unik += str(i)
#     jumlah_unik = len(unik)
#     return jumlah_unik

# print(unique_count([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
# print(unique_count([1, 1, 1, 1, 1, 1]))
# print(unique_count([]))

#================================================================

# angka_1 = int(input("Masukkan angka 1: "))
# angka_2 = int(input("Masukkan angka 2: "))

# if angka_1 * angka_2 > 1000:
#     hasil = angka_1 * angka_2
# else:
#     hasil = angka_1 + angka_2

# print(f"Hasilnya adalah: {hasil}")

#================================================================

# detik = int(input("Masukkan detik: "))
# jam = detik / 3600
# print(f"Detik dalam satuan jam: {jam:.2f}")
#================================================================

# def get_digits(num):
#     daftar_digit = []
#     for i in str(num):
#         daftar_digit.append(int(i))
#     return daftar_digit

# print(get_digits(2025))
# print(get_digits(6371293))
# print(get_digits(0))

#================================================================


# string = input("Masukkan input: ")
# for i in range(len(string)):
#     if i % 2 == 0:
#         print(string[i])
#================================================================

# nama = input("Masukkan nama: ")
# npm = input("Masukkan npm: ")
# print(f"Halo {npm} - {nama}! Salam kenal!")
#================================================================

# def remove_duplicates(lst):
#     tanpa_duplikat = []
#     for i in lst:
#         if i not in tanpa_duplikat:
#             tanpa_duplikat.append(i)
#     return tanpa_duplikat

# print(remove_duplicates([2, 7, -6, 2, 0, 7, 10, -1, -9, 3, -8]))
# print(remove_duplicates(['g', 't', 't', 'm', 's', 'j', 'i', 'v', 't', 'l', 'k', 't', 'p', 'z', 'z', 'l', 'd', 'e', 'l', 'p']))
# print(remove_duplicates([7, 5, 6, 1, 5, 5, 9, 2, 6, 0, 10, 4, 10, 10, 0]))

#================================================================

# tahun = int(input("Masukkan tahun: "))
# if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
#     print(f"Tahun {tahun} adalah tahun kabisat")
# else:
#     print(f"Tahun {tahun} bukanlah tahun kabisat")

#================================================================

# def camel_to_snake(var_name):
#     list_snake = []
#     tampung = ""
#     for i in range(len(var_name) - 1):
#         if var_name[i+1].islower():
#             tampung += var_name[i]
#         else:
#             tampung += var_name[i]
#             list_snake.append(tampung.lower())
#             tampung = ""
#     tampung += var_name[-1]
#     list_snake.append(tampung.lower())
#     return "_".join(list_snake)


# print(camel_to_snake("firstName"))
# print(camel_to_snake("age"))
# print(camel_to_snake("userInputTime"))

#================================================================

# def remove(elemen, lst):
#     hasil = []
#     for kar in lst:
#         if kar != elemen:
#             hasil.append(kar)
#     return list(hasil)

# print(remove(4, [1,4,7,4,8,9]))
# print(remove(5, []))
# print(remove(10, [1,3,5]))
# print(remove(7, [7,7,2,7]))

#================================================================

# def rotate_left3(nums):
#   hasil = nums[1:] + list(nums[0])
#   return hasil
# print(rotate_left3([1, 2, 3]))


# nums = [1,2,3]

# hasil = nums[1:] 
# angka = nums[0]
# print(hasil)
# print(list(angka))

# string = "budi santoso"
# nama = string.split()
# print(nama)

# def make_tags(tag, word):
#   return f"<{tag}>{word}</{tag}>"

# print(make_tags('i', 'Yay'))


# n = int(input("n: "))

# for i in range(1, n + 1):
#     for _ in range(n - i):
#         print(" ", end="")
#     for j in range(2*i - 1):
#         if j == 0 or j == 2*i - 2:
#             print("*", end="")
#         else:
#             print(" ", end="")
        
#     print()

# for i in range(1, n): # 1,2,3
#     for _ in range(i):
#         print(" ", end="")
#     for j in range((2*n - 1) - 2*i): # 5,3,1
#         if j == 0 or j == (2*n - 1) - 2*i - 1:
#             print("*", end="")
#         else:
#             print(" ",end="")
#     print()


# n = int(input("n: "))

# for i in range(1, n + 1): #1,2,3,4
#     for _ in range(n - i):
#         print(" ", end="")
#     for j in range(2 * i - 1): # 1,3,5,7
#         print("*", end="")
#     print()

# for i in range(1, n + 1):
#     for j in range(2 * n - 1):
#         if j == 0 or j == 2*n - 2:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# for i in range(n): #0,1,2,3
#     for _ in range(i):
#         print(" ", end="")
#     for x in range(2*n - 1-  2*i): # 7,5,3,1
#         print("*", end="")
#     print()


# def analisis_nilai(nilai):
#     rata = sum(nilai)/len(nilai)
#     diatas_rata = 0
#     for i in nilai:
#         if i > rata:
#             diatas_rata += 1
#     banyak_min = nilai.count(min(nilai))
#     selisih = max(nilai)- min(nilai)
#     return [rata, diatas_rata, banyak_min, selisih]

# print(analisis_nilai([60, 70, 80, 90]))

# def is_anagram(kata1, kata2):
#     kata1 = kata1.lower()
#     kata2 = kata2.lower()
#     sama = 0
#     for i in kata1:
#         if kata2.count(i) == kata1.count(i):
#             sama += 1
#     if sama == len(kata1):
#         return True
#     return False        
    


# print(is_anagram("Listen", "Silent"))
# print(is_anagram("Listen", "Silent"))
# print(is_anagram("Listen", "Silent"))

# LATIHAN SOAL 


# angka = [3, 1, 3, 1, 4, 0, 1]

# def frekuensi(angka):
#     hasil = {}
#     for chr in angka:
#         jumlah = angka.count(chr)
#         if chr not in hasil:
#             hasil[chr] = jumlah
#     return hasil

# print(frekuensi(angka))


# def posisi(angka):
#     hasil = {}
#     for i in range(len(angka)):
#         if angka[i] not in hasil:
#             hasil[angka[i]] = [i]
#         elif angka[i] in hasil:
#             hasil[angka[i]].append(i)
#     return hasil
# print(posisi(angka))


# nama = ["ani", "budi", "cici"]
# nilai = [90, 70, 85]

# rapor = dict(zip(nama, nilai))
# lulus = {}

# for nama, nilai in rapor.items():
#     if nilai >= 80:
#         lulus[nama] = nilai
# print(rapor)
# print(lulus)

# transaksi = [
#     ["roti", "susu", "roti"],
#     ["roti", "telur"],
#     ["susu", "kopi"]
# ]

# daftar_set = set()
# daftar_dict =  {}
# teman_belanja_roti = set()

# for belanjaan in transaksi:
#     for barang in belanjaan:
#         if barang not in daftar_set:
#             daftar_set.add(barang)
#         if barang not in daftar_dict:
#             daftar_dict[barang] = 1
#         else:
#             daftar_dict[barang] += 1
#     if "roti" in belanjaan:
#         teman_belanja_roti.update(set(belanjaan) - {"roti"})


# nama_toko = "Kopi Senja"         # global
# pajak = 0.1                      # global

# def hitung_total(harga):
#     # global pajak
#     pajak = pajak + 0.2
#     total = harga + harga * pajak
#     # return harga + harga * pajak
#     return total

# print(nama_toko)
# print(hitung_total(20000))

# total = 50

# def tes():
#     try:
#         # total = 10               # keberadaan baris ini membuat 'total' lokal di SELURUH fungsi
#         return total 
#         # print(total)
#         total = 10            # baris ini membaca 'total' LOKAL (belum terisi)
#     except UnboundLocalError as error:
#         print("Error:", error)

# tes()

saldo = 1000                     # global

def tarik(jumlah):
    # global saldo                 # "saldo yang kupakai adalah yang global"
    saldo = saldo - jumlah
    print("Saldo di fungsi:", saldo)

tarik(300)                       # 1000 - 300 = 700
tarik(200)                       # 700 - 200 = 500
print("Saldo akhir:", saldo)