#Buat Program Pengelola Daftar Buku yang disimpan dalam list.
#MEISHELLA NOER ALYSIA
#Kelas 01TPLP013

#Pertama, kita harus buat dulu variabel yang menyimpan listnya.
kumpulan_buku = []

#buat judul programnya
print("\n","="*10,"Mengelola Daftar Buku","="*10)
print("""1. Tambah Buku
2. Lihat Semua Buku
3. Cari Buku
4. Hapus Buku
5. Urutkan Buku
0. Keluar""")
#kita gunakan while True 
while True:

    #buat kode input pilihan penggunanya
    pilihan = input("Anda Ingin Melakukan Apa?(1/2/3/4/5) atau 0 untuk keluar: ")

    #lalu kita langsung buat match-case dari pilihan pengguna ya ges:
    match pilihan:
        case "1":
            #buat input menggunakan .strip().title() agar spasi lebih terhapus dan huruf besar hanya di awal untuk setiap kata
            buku_baru = input("\nMASUKKAN JUDUL BUKU BARU: ").strip().title()
            #kita buat kasus jika inputnya salah atau ada yang sama
            #kalo pengguna mengosongkan judul buku:
            if not buku_baru:
                print("\nJUDUL BUKU TIDAK BOLEH KOSONG\n")
                
            #kalo pengguna mengisi judul buku yang sudah ada: (pake any maksudnya agar mengecek ada bernilai true apa ga)
            elif any(judul.lower() == buku_baru.lower() for judul in kumpulan_buku):#.lower() untuk menyamakan huruf dikeduanya agar kecil semua
                print("\n JUDUL BUKU SUDAH ADA\n")
            else:
                kumpulan_buku.append(buku_baru)
                print(f"\nBuku dengan judul {buku_baru} telah ditambahkan\n")
                

        case "2":
            #jika kosong kita bilang kalo masih kosong 
            if not kumpulan_buku:
                print("\nMAAF BELUM ADA JUDUL BUKU YANG DI INPUT\n")
            else:
                print("\n","="*10,"Daftar Judul Buku","="*10)
                #kita pake for enumerate soalnya biar dia nge print semua yang ada di list kumpulan_buku
                for nomor,nama in enumerate(kumpulan_buku):
                    print(f"{nomor+1}. {nama}")

        case "3":
            #kita buatkan input pengguna nya dulu, pastikan ya pake .strip().lower() agar inputnya menghapus spasi lebih,
            #dan mengubah semua huruf menjadi huruf kecil
            kunci = input("\nJUDUL BUKU: ").strip().lower()
            #nah kita pake for loop buat menemukan judulnya
            #buat variabel baru dulu
            ketemu = False
            for nama in kumpulan_buku:
                if kunci in nama.lower():
                    print(f"\nDitemukan: {nama}")
                    ketemu = True
            #buat kondisi jika tidak ditemukan:
            if not ketemu:
                print("\nBuku tidak ditemukan!")

        case "4":
            if not kumpulan_buku:
                print("\nBELUM ADA BUKU YANG TERSEDIA SILAHKAN TAMBAH BUKU!\n")
            else:#jika ada buku yang tersedia, buatkan kondisi dengan try except
                try:
                    nomorbuku = int(input("\nMasukkan Nomor Buku yang Mau dihapus: "))
                    #agar python tidak membaca nomor dibawah 1 jadi urutan bawah, maka kita pakai:
                    if nomorbuku < 1 :
                        print("\nNOMOR GA VALID\n")
                    else:#kita hapus menggunakan pop(index) agar buku pada index tersebut terhapus
                        hapusbuku = kumpulan_buku.pop(nomorbuku - 1)
                        print(f"\nBuku {hapusbuku} sudah dihapus.\n")
                except:
                    print("\nNomor tidak valid!\n")

        case "5":
            #kita pakai kondisi jika buku belum ada dulu
            if not kumpulan_buku:
                print("\n","-"*10,"BELUM ADA BUKU","-"*10,"\n")

            #jika buku ada, maka kita gunakan sorted agar buku diurutkan sesuai abjad
            else:
                for i, nama in enumerate(sorted(kumpulan_buku)):
                    print(f"{i+1}, {nama}")

        case "0":
            #pengguna sudah selesai menggunakan program
            print("\nTerima kasih, program selesai\n")
            break
        case _:
            #jika input tidak ada sesuai dengan case diatas
            print("\nINPUT TIDAK VALID, INPUT (1/2/3/4/5), atau 0 untuk keluar!\n")



            

