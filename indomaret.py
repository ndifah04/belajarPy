print("SELAMAT DATANG DI INDOMARET \n SELAMAT BERBELANJAAA :)")

daftar_belanja=[]
daftar_harga=[]
daftar_jumlah=[]
daftar_kembalian=[]

while True:
    print("=====pilih belanjaan anda :=====")
    print("1.klin : 5000 \n2.Daia : 10.000 \n3.Jaz1 : 15.000 \n4.Attack : 20.000 \n5.Rinso : 25.000 \n6.Sayang : 30.000")
    barang=str(input("pilih barang belanjaan anda : "))
    daftar_belanja.append(barang)
    jumlah=int(input("masukkan jumlah barang belanjaan anda : "))
    uang=int(input("masukkan uang anda : "))

    if barang=="klin":
        total=jumlah*5000
        daftar_harga.append(uang)
        daftar_jumlah.append(jumlah)

    elif barang=="daia":
        total=jumlah*10000
        daftar_harga.append(uang)
        daftar_jumlah.append(jumlah)

    elif barang=="jaz1":
        total=jumlah*10000
        daftar_harga.append(uang)
        daftar_jumlah.append(jumlah)

    elif barang=="attack":
        total=jumlah*20000
        daftar_harga.append(uang)
        daftar_jumlah.append(jumlah)

    elif barang=="rinso":
        total=jumlah*25000
        daftar_harga.append(uang)
        daftar_jumlah.append(jumlah)

    else:
        total=jumlah*30000
        daftar_harga.append(uang)
        daftar_jumlah.append(jumlah)

    print("===NOTA ANDA===")
    print("barang belanjaan :",daftar_belanja)
    print("jumlah barang :",daftar_jumlah)
    print("total brlanjaan :",daftar_harga)


    if uang>total:
        kembalian=uang-total
        daftar_kembalian.append(kembalian)
        print("kembalian anda :",kembalian)
        print("===TERIMA KASIH===")
    elif uang<total:
        print("uang anda tidak cukup")
    else:
        print("kembalian anda :0 ")
        print("===TERIMA KASIH===")

    pilih=str(input("masih mau ki belanja? y/n : "))
    if pilih=="y":
        continue
    else:
        break
# for i in range(len(daftar_harga)):
#     uang+=daftar_harga[i]
