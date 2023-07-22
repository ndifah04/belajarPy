# # KONVERSI SUHU (Fahrenheit, Reamur, Kelvin, Celcius)
# print("=========================KONVERSI SUHU==================== =======")
# print("______________________")
# print("Pilih Konversi : \n1. Fahrenheit \n2. Reamur \n3. Kelvin")
# konversi = input("Pilih Konversi yang diinginkan : ")

# if konversi == "1" :
#     C = input("Masukkan Suhu : ")
#     C = float(C)
#     suhu = ((9/5 * C) + 32)
#     print("Hasil konversi suhu dari celcius ke Fahrenheit adalah :", suhu)
# elif konversi == "2"  :
#     C = input("Masukkan Suhu : ")
#     C = float(C)
#     suhu = (4/5 * C)
#     print("Hasil konversi suhu dari celcius ke Reamur adalah :", suhu)
# elif konversi == "3" :
#     C = input("Masukkan Suhu : ")
#     C = float(C)
#     suhu = (C + 273.15)
#     print("Hasil konversi suhu dari celcius ke Kelvin adalah :", suhu)
# else :
#     print("Pilihan konversi anda tidak tersedia")
    
# # MENCARI LUAS PERSEGI PANJANG
# print("==================MENCARI LUAS PERSEGI PANJANG====================")
# print("______________________")

# panjang = input("Masukkan nilai panjang persegi panjang : ")
# panjang = float(panjang)

# lebar = input("Masukkan lebar persegi panjang : ")
# lebar = float(lebar)
    
# luas = 0.5 * panjang * lebar
# print("Luas Persegi panjang adalah ", luas)
    
# # TIPE DATA DARI BAHASA C
# print("=======KONVERSI TIPE DATA BOOLEAN KE PYTHON DARI BAHASA C=========")
# print("______________________")

# from ctypes import c_double
# data_c_double = c_double(10.5)
# print("Ini tipe data ", type(data_c_double), "Contohnya adalah ",data_c_double)
