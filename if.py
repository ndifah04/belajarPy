# KONDISI DAN PERULANGAN
# nama="nabila"
# if nama =="nabila":
#     print(f" {nama} namaku")
#     # print(nama,"namaku")
# else:
#     print("nama",nama,"tidak ditemukan")
# ------------------------------------------------------------------------------------------
# id=str(input("masukkan id anda: "))
# sandi=int(input("masukkan sandi anda: "))

# if id =="difah"and sandi==4444:
#     print("selamat anda berhasil login")

# elif id !="difah" and sandi==4444:
#     print("sandi yang anda masukkan salah")

# elif id =="difah" and sandi!=4444:
#     print("sandi yang anda masukkan salah")

# else:
#     print("id dan sandi anda salah")

# ------------------------------------------------------------------------------------------
# data= input("nama :")
# while data:
#     if data== "cu":
#         print("sukses")
#         print("apakah kamu mau lanjut atau tdk y/t ?")
#         data1= input("lanjut?")
#         if data1=="y":
#             print("sukses")
#             continue
#         else:
#             print("ok")
#             break
#     else:
#         print("okdeh")
#         break
# ------------------------------------------------------------------------------------------
# operator= str(input("masukkan operator: + - x : %  "))
# nilai1=int(input("masukkan nilai 1 :"))
# nilai2=int(input("masukkan nilai 2 :"))

# if operator== "+":
#     hasil= nilai1+nilai2
#     print(nilai1,"+",nilai2,"=",hasil)

# elif operator== "-":
#     hasil= nilai1-nilai2
#     print(nilai1,"-",nilai2,"=",hasil)

# elif operator== "x":
#     hasil= nilai1*nilai2
#     print(nilai1,"x",nilai2,"=",hasil)

# elif operator== ":":
#     hasil= nilai1//nilai2
#     print(nilai1,":",nilai2,"=",hasil)

# elif operator== "%":
#     hasil= nilai1%nilai2
#     print(nilai1,"%",nilai2,"=",hasil)
# else:
#     print("operator yang anda massukan tidak tersedia :)")
# ------------------------------------------------------------------------------------------
# IF DALAM IF

# data=10
# if data==10:
#     hasil=data+data
#     if hasil >=20:
#         print("hasil=",hasil)
#     elif hasil <=20:
#         print("hasil=",hasil)
#     else:
#         print("ok")

# elif data<=10:
#     hasil=data+data
#     if hasil >=20:
#         print("hasil=",hasil)
#     elif hasil <=20:
#         print("hasil=",hasil)
#     else:
#         print("ok")
# ------------------------------------------------------------------------------------------
# PROGRAM LAUNDRY
# print(" 1. cuci biasa = 4000 \n 2. cuci lipat = 5000 \n 3. lipat + setrika = 7000 \n 4. cuci lipat + setrika + parfum = 8000 \n 5. ekspres = 10.000")

# paket=str(input("pilih paket anda "))
# berat=int(input("masukkan berat cucian "))
# nama=str(input("masukkan nama anda "))
# alamat=str(input("masukkan alamat anda "))
# bayar=int(input("masukkan uang anda "))

# if paket== "1":
#     total=berat*4000
#     if berat>=10:
#         diskon= total*10/100
#         kembalian = int (bayar - total)
#         print("----NOTA ANDA----")
#         print("uang anda= ",bayar)
#         print("harga perkilo 4000")
#         print("berat cucian anda=",berat, "kg")
#         print("nama=", nama)
#         print("alamat=",alamat)
#         print("total bayar anda=",total-diskon)
#         print("anda mendapatkan diskon sebesar=",diskon)
#         print("kembalian anda=", kembalian)
#         print("----TERIMA KASIH----")
#     elif berat <10 and berat >5:
#         kembalian = int (bayar - total)
#         print("----NOTA ANDA----")
#         print("uang anda= ",bayar)
#         print("harga perkilo 4000")
#         print("berat cucian anda=",berat, "kg")
#         print("nama=", nama)
#         print("alamat=",alamat)
#         print("total bayar anda=",total)
#         print("kembalian anda=", kembalian)
#         print("sekamat anda mendapatkan kupon")
#         print("----TERIMA KASIH----")
#     else:
#         kembalian = int (bayar - total)
#         print("----NOTA ANDA----")
#         print("uang anda= ",bayar)
#         print("harga perkilo 4000")
#         print("berat cucian anda=",berat, "kg")
#         print("nama=", nama)
#         print("alamat=",alamat)
#         print("total bayar anda=",total)
#         print("kembalian anda=",kembalian)
#         print("----TERIMA KASIH----")

# elif paket== "2":
#     total=berat*5000
#     if berat>=10:
#         diskon= total*10/100
#         kembalian = int (bayar - total)
#         print("----NOTA ANDA----")
#         print("uang anda= ",bayar)
#         print("harga perkilo 5000")
#         print("berat cucian anda=",berat, "kg")
#         print("nama=", nama)
#         print("alamat=",alamat)
#         print("total bayar anda=",total-diskon)
#         print("anda mendapatkan diskon sebesar=",diskon)
#         print("kembalian anda=", kembalian)
#         print("----TERIMA KASIH----")
#     elif berat <10 and berat >5:
#         kembalian = int (bayar - total)
#         print("----NOTA ANDA----")
#         print("uang anda= ",bayar)
#         print("harga perkilo 5000")
#         print("berat cucian anda=",berat, "kg")
#         print("nama=", nama)
#         print("alamat=",alamat)
#         print("total bayar anda=",total)
#         print("kembalian anda=", kembalian)
#         print("sekamat anda mendapatkan kupon")
#         print("----TERIMA KASIH----")
#     else:
#         kembalian = int (bayar - total)
#         print("----NOTA ANDA----")
#         print("uang anda= ",bayar)
#         print("harga perkilo 5000")
#         print("berat cucian anda=",berat, "kg")
#         print("nama=", nama)
#         print("alamat=",alamat)
#         print("total bayar anda=",total)
#         print("kembalian anda=", kembalian)
#         print("----TERIMA KASIH----")

# elif paket== "3":
#     total=berat*7000
#     if berat>=10:
#         diskon= total*10/100
#         kembalian = int (bayar - total)
#         print("----NOTA ANDA----")
#         print("uang anda= ",bayar)
#         print("harga perkilo 7000")
#         print("berat cucian anda=",berat, "kg")
#         print("nama=", nama)
#         print("alamat=",alamat)
#         print("total bayar anda=",total-diskon)
#         print("anda mendapatkan diskon sebesar=",diskon)
#         print("kembalian anda=", kembalian)
#         print("----TERIMA KASIH----")
#     elif berat <10 and berat >5:
#         kembalian = int (bayar - total)
#         print("----NOTA ANDA----")
#         print("uang anda= ",bayar)
#         print("harga perkilo 7000")
#         print("berat cucian anda=",berat, "kg")
#         print("nama=", nama)
#         print("alamat=",alamat)
#         print("total bayar anda=",total)
#         print("kembalian anda=",kembalian)
#         print("sekamat anda mendapatkan kupon")
#         print("----TERIMA KASIH----")
#     else:
#         kembalian = int (bayar - total)
#         print("----NOTA ANDA----")
#         print("uang anda= ",bayar)
#         print("harga perkilo 7000")
#         print("berat cucian anda=",berat, "kg")
#         print("nama=", nama)
#         print("alamat=",alamat)
#         print("total bayar anda=",total)
#         print("kembalian anda=", kembalian)
#         print("----TERIMA KASIH----")

# elif paket== "4":
#     total=berat*8000
#     if berat>=10:
#         diskon= total*10/100
#         kembalian = int (bayar - total)
#         print("----NOTA ANDA----")
#         print("uang anda= ",bayar)
#         print("harga perkilo 8000")
#         print("berat cucian anda=",berat, "kg")
#         print("nama=", nama)
#         print("alamat=",alamat)
#         print("total bayar anda=",total-diskon)
#         print("anda mendapatkan diskon sebesar=",diskon)
#         print("kembalian anda=", kembalian)
#         print("----TERIMA KASIH----")
#     elif berat <10 and berat >5:
#         kembalian = int (bayar - total)
#         print("----NOTA ANDA----")
#         print("uang anda= ",bayar)
#         print("harga perkilo 8000")
#         print("berat cucian anda=",berat, "kg")
#         print("nama=", nama)
#         print("alamat=",alamat)
#         print("total bayar anda=",total)
#         print("kembalian anda=", kembalian)
#         print("sekamat anda mendapatkan kupon")
#         print("----TERIMA KASIH----")
#     else:
#         kembalian = int (bayar - total)
#         print("----NOTA ANDA----")
#         print("uang anda= ",bayar)
#         print("harga perkilo 8000")
#         print("berat cucian anda=",berat, "kg")
#         print("nama=", nama)
#         print("alamat=",alamat)
#         print("total bayar anda=",total)
#         print("kembalian anda=", kembalian)
#         print("----TERIMA KASIH----")

# elif paket== "5":
#     total=berat*5000
#     if berat>=10:
#         diskon= total*10/100
#         kembalian = int (bayar - total)
#         print("----NOTA ANDA----")
#         print("uang anda= ",bayar)
#         print("harga perkilo 10.000")
#         print("berat cucian anda=",berat, "kg")
#         print("nama=", nama)
#         print("alamat=",alamat)
#         print("total bayar anda=",total-diskon)
#         print("anda mendapatkan diskon sebesar=",diskon)
#         print("kembalian anda=", kembalian)
#         print("----TERIMA KASIH----")
#     elif berat <10 and berat >5:
#         kembalian = int (bayar - total)
#         print("----NOTA ANDA----")
#         print("uang anda= ",bayar)
#         print("harga perkilo 10.000")
#         print("berat cucian anda=",berat, "kg")
#         print("nama=", nama)
#         print("alamat=",alamat)
#         print("total bayar anda=",total)
#         print("kembalian anda=", kembalian)
#         print("sekamat anda mendapatkan kupon")
#         print("----TERIMA KASIH----")
#     else:
#         kembalian = int (bayar - total)
#         print("----NOTA ANDA----")
#         print("uang anda= ",bayar)
#         print("harga perkilo 10.000")
#         print("berat cucian anda=",berat, "kg")
#         print("nama=", nama)
#         print("alamat=",alamat)
#         print("total bayar anda=",total)
#         print("kembalian anda=", kembalian)
#         print("----TERIMA KASIH----")

# if bayar < total:
#     print("anda berhutang sebesar", kembalian)
#     lagi=int(input("masukkna uang lagi"))

# ------------------------------------------------------------------------------------------
# GAJI KARYAWAN
# print("pilih golongan anda \n golongan 1 \n golongan 2 \n golongan 3")
# golongan=str(input("masukkan golongan anda= "))
# # jam kerja wajib 160/bulan
# nama=str(input("masukkan nama anda= "))
# jam=int(input("masukkan jam kerja anda= "))
# lembur=15000*jam

# gaji=2000000

# if golongan=="1":
#     total= int(0.05*gaji+lembur)
#     print("golongan 1")
#     print("nama karyawan:",nama)
#     print("jumlah jam kerja:",jam)
#     print("total gaji anda:",total)

# elif golongan== "2":
#     total= int (0.1*gaji+lembur)
#     print("golongan 1")
#     print("nama karyawan:",nama)
#     print("jumlah jam kerja:",jam)
#     print("total gaji anda:",total)

# elif golongan== "3":
#     total= int (0.15*gaji+lembur)
#     print("golongan 1")
#     print("nama karyawan:",nama)
#     print("jumlah jam kerja:",jam)
#     print("total gaji anda:",total)

# else:
#     print("golongan yang anda masukkan tidak ada")
# ------------------------------------------------------------------------------------------
# PERULANGAN
# for i in range(10):
#     print(i)

# i=1
# while i <= 10:
#     print(i)
#     i+=1

# i=1
# while i<=20:
#     kali = i * 2
#     print(i,"x2=",kali)
#     i+=1

# for i in range(7 ):
#     i = i*2
#     print(i)
    

# i=1
# while i<=10:
#     kali = i * 5
#     print(i,"x5=",kali)
#     i+=1
# ------------------------------------------------------------------------------------------

