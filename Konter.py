# Tugas aplikasi_Konter hp

print("--------------------------------------")
print("Khall_Chell")
print("Jl. Moh Hatta No. 03")
print("--------------------------------------")
bayar = int(input("Masukan jumlah bayar             Rp. "))

def beli_pulsa(p):
    global bayar
    if bayar >= int(p):
        bayar -= int(p)
        print("--------------------------------------")
        print("No. Handphone              :", no_hp)
        print("Berhasil Membeli Pulsa   Rp.",p)
        print("Sisa Saldo               Rp.", bayar)
        print("--------------------------------------")
        print("Terimakasih atas kunjungannya")
        print("--------------------------------------")
    else:
        print("Ops Saldo Anda Kurang")

Lanjut_beli = "y" 
while Lanjut_beli == "y" :
    no_hp = int(input("Masukan nomer handphone anda       : "))
    print("--------------------------------------")
    print("1.Beli pulsa Rp.10.000")
    print("2.Beli Pulsa Rp.20.000")
    print("3.Beli Pulsa Rp.30.000")
    print("4.Beli Pulsa Custom")
    print("5.Keluar aplikasi")
   
    a = int(input("Silahkan pilih pulsa yang mau di beli : "))
    if a == 1:
        beli_pulsa(10.000)
    elif a == 2:
        beli_pulsa(20.000)
    elif a == 3:
        beli_pulsa(30.000)
    elif a == 4:
        beli_pulsa(input("Silahkan masukukan nominal yang di inginkan Rp."))
    elif a == 5:
        Lanjut_beli = "n"
    else:
        print("Pilihan tidak tersedia")
    break