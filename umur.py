nama = (input("masukkan nama :"))
tahun_lahir = (input("masukkan tahun lahir :"))

index1 = tahun_lahir[0]
index4 = tahun_lahir[3]

index1 = int(index1)
index4 = int(index4)
hasil = index1 * index4
hasil1 = hasil * 7 * 1000

print("Nama         : ", nama)
print("Tahun lahir  : ", tahun_lahir)
print("Jajan perminggu : ",hasil1,)