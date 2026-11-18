#Buat Program Kasir Parkir yang mencatat kendaraan keluar satu per satu, lalu menampilkan rekap pendapatan terakhir
#Meishella Noer Alysia 
#Kelas 01TPLP013

#kita buat dulu variabel jumlah_motor, jumlah_mobil, jumlah_truk, dan total_pendapatan agar bisa dihitung 
jumlah_motor = 0
jumlah_mobil = 0
jumlah_truk = 0
total_pendapatan = 0

#buat perulangannya menggunakan while True
while True:
    print("===============KASIR PARKIR==============")
    print("---------Gunakan dengan jujur ya---------")

    #buat inputnya dulu, agar menghemat ketikan, kita gunakan
    #.strip().upper() agar huruf yang terinput berubah jadi kapital dan semua spasi kosong hilang
    kendaraan = input("Jenis kendaraan(M/B/T), atau X=tutup :").strip().upper()

    #kita buat kondisi kalo pengguna mengetik X, atau tidak sesuai dulu, biar input waktu gausah jalan programnya
    match kendaraan:
        case "X":
            break #jadi langsung ke tampilan akhir
        case "M" | "B" | "T":
            pass #nah ini lanjut ke program selanjutnya
        case _:
            print("Jenis kendaraan tidak tersedia, input (M/B/T), atau X untuk tutup kasir\n")
            continue

    #input waktu kendaraan 
    waktu = int(input("Lama parkir kendaraan                :"))#agar hasilnya berupa integer

    #kita buat kondisi kalo pengguna menginput waktu parkir kurang dari atau sama dengan 0:
    if waktu <= 0:
        print("Waktu harus lebih dari 0 ya!\n")
        continue

    #nah baru kita buat match-case jika input an semua sudah valid
    match kendaraan:
        #buat kondisi pertama jika memilih motor 
        case "M":
            #waktu kita kurang 1 dan dikali 1000 lalu kita tambah dengan jam pertama itu (2000)
            biaya = 2000 + (waktu - 1) * 1000 
            #kita tampilkan biaya parkirnya:
            print(f"Biaya Parkir                         :Rp.{biaya}\n")
            #kita tambah variabel yang di awal agar semua ketotal:
            jumlah_motor += 1
            total_pendapatan += biaya

        #buat kondisi kedua jika memilih mobil 
        case "B":
            #waktu kita kurang 1 dan dikali 3000 lalu kita tambah dengan jam pertama itu (5000)
            biaya = 5000 + (waktu - 1) * 3000 
            #kita tampilkan biaya parkirnya:
            print(f"Biaya Parkir                         :Rp.{biaya}\n")
            #kita tambah variabel yang di awal agar semua ketotal:
            jumlah_mobil += 1
            total_pendapatan += biaya

        #buat kondisi ketiga jika memilih truk 
        case "T":
            #waktu kita kurang 1 dan dikali 5000 lalu kita tambah dengan jam pertama itu (10000)
            biaya = 10000 + (waktu - 1) * 5000 
            #kita tampilkan biaya parkirnya:
            print(f"Biaya Parkir                         :Rp.{biaya}\n")
            #kita tambah variabel yang di awal agar semua ketotal:
            jumlah_truk += 1
            total_pendapatan += biaya


#kita buat rekap nya di bawah sini:
print("\n","="*10,"REKAP PARKIR", "="*10)
print(f"""Total Motor     : {jumlah_motor}
Total Mobil     : {jumlah_mobil}
Total Truk      : {jumlah_truk}
Total Pendapatan: Rp.{total_pendapatan}

TERIMA KASIH, PROGRAM SELESAI
""")
          

