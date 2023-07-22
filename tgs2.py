# TUGAS ARINI
print("==========TUGAS MEMBUAT DATA PELANGGAN DAN TAHUN LAHIR============")
print("______________________")

tahun = int(input("Masukkan Tahun Lahir 1 : "))
belanja = int(input("Masukkan Belanja anda Rp. "))

tahun1 = int(input("Masukkan Tahun Lahir 1 : "))
belanja1 = int(input("Masukkan Belanja anda Rp. "))

spasi = 5* " "
print("------------------------------------------------------------------")
print("|", spasi, "Data Pelanggan Dengan Tahun Lahir", spasi*4, "  |")
print("------------------------------------------------------------------")

diskon1 = (tahun/1000) * (tahun % 100)
diskon1 = int(diskon1)

diskon2 = (tahun1/1000) * (tahun1 % 100)
diskon2 = int(diskon2)

bayar1 = belanja - (belanja * diskon1) / 100
bayar1 = int(bayar1)

bayar2 = belanja1 - (belanja1 * diskon2) / 100
bayar2 = int(bayar2)

print("|  1. |", tahun , " Total Belanja Rp. ", belanja, spasi*4, "   |")
print("|  2. |", tahun1 , " Total Belanja Rp. ", belanja1, spasi*4, "   |")
print("==================================================================")

print("------------------------------------------------------------------")
print("|  NO |", spasi, "  Masukkan  |", spasi, "   Keluaran   ", spasi*2, "     |")
print("------------------------------------------------------------------")
print("|  1. |", tahun, spasi*2 ,"  |", "Besar Diskon ", diskon1, "%", spasi*3,"   |")
print("|     |", belanja, spasi, "       |", "Jumlah yang dibayar Rp. ", bayar1, "     |")
print("------------------------------------------------------------------")
print("|  2. |", tahun,spasi*2 ,"  |", "Besar Diskon ", diskon2, "%", spasi*3,"  |")
print("|     |", belanja1, spasi, "       |", "Jumlah yang dibayar Rp. ", bayar2,"    |")
print("------------------------------------------------------------------")