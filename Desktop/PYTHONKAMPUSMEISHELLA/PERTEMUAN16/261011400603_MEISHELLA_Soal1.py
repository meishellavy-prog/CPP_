#PROGRAM MENU KONVERSI SUHU YANG BERJALAN TERUS SAMPAI PENGGUNA MEMILIH UNTUK BERHENTI.
#MEISHELLA NOER ALYSIA 
#KELAS 01TPLP013

banyak_konversi = 0 #ini variabel agar kita bisa menghitung berapa kali pengguna melakukan konversi suhu
while True:
    #Buat judul program dan pilihan, ini akan membantu pengguna untuk memilih dan jika ingin berhenti
    print("=== PROGRAM KONVERSI SUHU ===")
    print("1. Celcius -> Fahrenheit")
    print("2. Celcius -> Kelvin")
    print("3. Celcius -> Reamur")
    print("4. Fahrenheit -> Celcius")
    print("0. Keluar")
    print("==============================")

    #buat input untuk pengguna memilih 
    pilihan = input("Pilih Konversi Anda (1/2/3/4) atau 0 untuk keluar: ")

    #buat kondisi untuk setiap pilihan pengguna menggunakan match-case
    match pilihan:
        case "1": #kita buat kondisi untuk konversi Celcius ke Fahrenheit

            #input suhu dalam celcius, pakai float agar bisa menerima angka desimal
            celcius = float(input("Masukkan suhu dalam Celcius                      : "))
            #lakukan konversi ke Fahrenheit dengan rumus (C * 9/5) + 32
            fahrenheit = (celcius * 9/5) + 32
            #tampilkan hasil konversi
            print(f"\nHASIL: {celcius:.2f} Celcius = {fahrenheit:.2f} Fahrenheit\n")#:.2f untuk 2 angka dibelakang koma
            banyak_konversi += 1 #tambah 1 ke variabel banyak_konversi 

        case "2": #kita buat kondisi untuk konversi Celcius ke Kelvin

            #input suhu dalam Celcius
            celcius = float(input("Masukkan suhu dalam Celcius                      : "))
            #lakukan konversi ke Kelvin dengan rumus C + 273.15
            kelvin = celcius + 273.15
            #tampilkan hasil konversi
            print(f"\nHASIL: {celcius:.2f} Celcius = {kelvin:.2f} Kelvin\n")#sama kayak tadi, 2 angka dibelakang koma
            banyak_konversi += 1 #tambah 1 ke variabel banyak_konversi

        case "3": #kita buat kondisi untuk konversi Celcius ke Reamur
        
            #input suhu dalam Celcius
            celcius = float(input("Masukkan suhu dalam Celcius                      : "))
            #lakukan konversi ke Reamur dengan rumus C * 4/5
            reamur = celcius * 4/5
            #tampilkan hasil konversi
            print(f"\nHASIL: {celcius:.2f} Celcius = {reamur:.2f} Reamur\n")#sama kayak tadi, 2 angka dibelakang koma
            banyak_konversi += 1 #tambah 1 ke variabel banyak_konversi

        case "4": #kita buat kondisi untuk konversi Fahrenheit ke Celcius
            
            #input suhu dalam Fahrenheit
            fahrenheit = float(input("Masukkan suhu dalam Fahrenheit                   : "))
            #lakukan konversi ke Celcius dengan rumus (F - 32) * 5/9
            celcius = (fahrenheit - 32) * 5/9
            #tampilkan hasil konversi
            print(f"\nHASIL: {fahrenheit:.2f} Fahrenheit = {celcius:.2f} Celcius\n")
            banyak_konversi += 1 #tambah 1 ke variabel banyak_konversi

        case "0": #kita buat kondisi untuk keluar dari program
            print("\nTerima kasih ya sudah menggunakan program ini! -Meishella Noer Alysia\n")
            #kita tampilkan berapa kali pengguna melakukan konversi
            print (f"Anda telah melakukan konversi sebanyak : {banyak_konversi} kali\n")
            break #keluar dari loop while True
        #buat kondisi jika pengguna memasukkan pilihan yang tidak valid
        case _:
            print("\nPilihan tidak valid! Silahkan pilih 1/2/3/4 atau 0 untuk keluar.\n")






