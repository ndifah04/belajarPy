# BUAT PROGRAM BANK BRI

print("PILIH BAHASA \n 1.BAHASA INDONESIA \n 2.BAHASA INGRIS \n")
bhs=str(input("pilih bahasa yang anda :"))
saldo=1000000
if bhs=="1":
    pin=int(input("masukkan pin anda :"))
    if pin == 122333:
        print("MENU UTAMA \n 1.RP 100.000 \n 2.RP 300.000 \n 3.RP 500.000 \n 4.1000.000 \n 5. penarikan jumlah lainnya \n 6.trasfer \n 7.menu lain")
        menu=str(input("pilih menu anda "))
        if menu=="1":
            sisa=saldo-100000
            print("=====================NOTA==================")
            print("anda akan menarik saldo sebesar 100.000")
            print("saldo awal anda: ",saldo)
            print("sisa saldo anda: ",sisa)
            print("===============TERIMAKASIH=================")
        elif menu=="2":
            sisa=saldo-300000
            print("=====================NOTA==================")
            print("anda akan menarik saldo sebesar 300.000")
            print("saldo awal anda: ",saldo)
            print("sisa saldo anda: ",sisa)
            print("===============TERIMAKASIH=================")
        elif menu=="3":
            sisa=saldo-500000
            print("=====================NOTA==================")
            print("anda akan menarik saldo sebesar 500.000")
            print("saldo awal anda: ",saldo)
            print("sisa saldo anda: ",sisa)
            print("===============TERIMAKASIH=================")
        elif menu=="4":
            sisa=saldo-1000000
            print("=====================NOTA==================")
            print("anda akan menarik saldo sebesar 1000.000")
            print("saldo awal anda: ",saldo)
            print("sisa saldo anda: ",sisa)
            print("===============TERIMAKASIH=================")
        elif menu=="5":
            print("PENARIKAN JUMLAH LAINNYA")
            jumlah=int(input("masukkan jumlah penarikan :"))
            if jumlah<saldo:
                saldo= saldo-jumlah
                print("=====================NOTA==================")
                print("jumlah penariakan: ",jumlah)
                print("sisa saldo anda  : ",saldo)
                print("penarikan anda sukses")
                print("===============TERIMAKASIH=================")
            else:
                print("saldo anda tidak cukup :)")
        elif menu=="6":
            print("TRASFER")
            jumlah=int(input("masukkan jumlah pengiriman :"))
            if jumlah<saldo:
                saldo= saldo-jumlah
                print("=====================NOTA==================")
                print("jumlah pengiriman: ",jumlah)
                print("sisa saldo anda  : ",saldo)
                print("pengiriman anda sukses")
                print("===============TERIMAKASIH=================")
        elif menu=="7":
            print("MENU LAIN \n 1. info saldo \n 2. isi saldo \n 3. ganti pin")
            menulain=str(input("masukkan pilihan anda :"))
            if menulain=="1":
                print("=====================NOTA==================")
                print("INFO SALDO ANDA")
                print("saldo anda sebesar  : ",saldo)
                print("===============TERIMAKASIH=================")
            elif menulain=="2":
                print("isi saldo")
                isi=int(input("masukkan saldo anda: "))
                print("=====================NOTA==================")
                total=isi+saldo
                print("isi saldo anda sekarang sebesar: ",total)
                print("===============TERIMAKASIH=================")
            elif menulain=="3":
                print("GANTI PIN")
                pin=int(input("masukkan sandi lama anda: "))
                if pin == 122333:
                    pinbaru=int(input("masukkan sandi baru anda: "))
                    print("sandi anda berhasil di ganti")
                else:
                    print("sandi lama yang anda masukkan salah")
    else:
            print("mohon maaf pin yang anda masukkan salah")
elif bhs=="2":
    print("MOHON MAAF \n belum pintar pa bahasa ingris")
else:
    print("pilihan yang anda masukkan tidak tersedia")
