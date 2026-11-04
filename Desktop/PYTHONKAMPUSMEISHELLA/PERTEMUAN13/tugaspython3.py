print("SOAL NOMOR 2 \n")
print("MEISHELLA NOER ALYSIA/01TPLP013\n")

print("="*5,"TARIF TIKET","="*5)
umur = int(input("Masukkan Umur Anda : "))
if umur <= 12:
    print("Tarif Tiket Anda Adalah: Rp20.000")
elif umur > 12 and umur <60:
    print("Tarif Tiket Anda Adalah: Rp50.000")
elif umur >=60:
    print("Tarif Tiket Anda AdalahL: Rp30.000")
else:
    print("Umur Tidak Valid")
