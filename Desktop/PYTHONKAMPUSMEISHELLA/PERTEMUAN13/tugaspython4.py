print("SOAL NOMOR 3 \n")
print("MEISHELLA NOER ALYSIA/01TPLP013\n")

print("="*5,"DAFTAR AKUN ANDA","="*5)
username = input("Masukkan Username Anda : ")
password = input("Masukkan Password Anda : ")
print("DATA ANDA SUDAH DISIMPAN \n")
print("="*5, "LOGIN KE AKUN ANDA","="*5)
username2 = input("Masukkan Username Anda : ")
password2 = input("Masukkan Password Anda : ")

if username2 == username and password2 == password:
    print("Login Berhasil Selamat Datang", username2)
else:
    print("Login Gagal, Username atau Password Anda Salah")
