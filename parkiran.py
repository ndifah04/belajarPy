# #PROGRAM PARKIRAN
# print("SELAMAT DATANG \n silahkan parkir \n pilih jenis kendaraan \n 1.motor=1000/jam \n 2.mobil=5000/jam")
# jenis=str(input("masukkan jenis kendaraan anda: "))
# if jenis=="1":
#     jam=int(input("lama parkir anda: "))
#     harga=jam*1000
#     print("jenis kendaraan anda       : Motor")
#     print("lama parkir anda           :",jam,"jam")
#     print("total bayar anda adalah    :",harga,) 
# elif jenis=="2":
#     jam=int(input("lama parkir anda: "))
#     harga=jam*5000
#     print("jenis kendaraan anda       : Mobil")
#     print("lama parkir anda           :",jam,"jam")
#     print("total bayar anda adalah    :",harga,) 
# else:
#     print("pilihan tidak tersedia")

#PROGRAM PARKIRAN
print("SELAMAT DATANG \n silahkan parkir \n pilih jenis kendaraan \n 1.motor=1000/jam \n 2.mobil=5000/jam")
jenis=str(input("masukkan jenis kendaraan anda: "))
jam_masuk=int(input("masukkan jam masuk parkir anda: "))
jam_keluar=int(input("masukkan jam keluar anda: "))
jam=jam_keluar-jam_masuk
if jenis=="1":
    harga=jam*1000
    if jam <1:
        print("jenis kendaraan anda       : Motor")
        print("jam parkir masuk anda      : ",jam_masuk,"jam")
        print("jam parkir keluar anda     : ",jam_keluar,"jam")
        print("total bayar anda adalah    :1000") 
    else:
        print("jenis kendaraan anda       : Motor")
        print("jam parkir masuk anda      : ",jam_masuk,"jam")
        print("jam parkir keluar anda     : ",jam_keluar,"jam")
        print("lama parkir anda           : ",jam,"jam")
        print("total bayar anda adalah    : ",harga,)  
elif jenis=="2":
    harga=jam*5000
    if jam <1:
        print("jenis kendaraan anda       : Mobil")
        print("jam parkir masuk anda      : ",jam_masuk,"jam")
        print("jam parkir keluar anda     : ",jam_keluar,"jam")
        print("total bayar anda adalah    :5000") 
    else:
        print("jenis kendaraan anda       : Mobil")
        print("jam parkir masuk anda      : ",jam_masuk,"jam")
        print("jam parkir keluar anda     : ",jam_keluar,"jam")
        print("lama parkir anda           : ",jam,"jam")
        print("total bayar anda adalah    : ",harga,)  
else:
    print("pilihan tidak tersedia")