// int main(){
    //     cout << "Hello kelas 01TPLP013"<< endl;
    //     cout << "Selamat belajar Algoritma dan Pemrograman dasar"<< endl;
    //     //BIODATA:
    //     cout << "berikut biodata saya:"<< endl;
    //     cout << "Nama: Meishella Noer Alysia" << endl;
    //     cout << "Kelas: 01TPLP013" << endl;
    //     cout << "Alamat: Jl. Poncol gang II rt.001/rw.004" << endl;
    //     cout << "Tempat, Tanggal Lahir: Jakarta, 19 Mei 2007" << endl;
    //     return 0;
    // }
    
    #include <iostream>
    using namespace std;
//tugas 3 tanggal 16 September 2026 
//algoritma dan pemrograman dasar
//Meishella Noer Alysia
//01TPLP013
//Bukti program 7 + 3*2 - (8%3) = 11 adalah sebagai berikut:
int main() {
    int result = 7 + 3 * 2 - (8 % 3);
    cout << "Hasil dari 7 + 3*2 - (8%3) = " << result << endl;  
//program konversi suhu celcius ke fahrenheit menggunakan rumus F = (C * 9/5) + 32
    double celsius, fahrenheit;//kenapa ga float? karena float itu kurang presisi, double lebih presisi
    cout << "Masukkan suhu dalam Celcius: ";
    cin >> celsius;
    fahrenheit = (celsius * 9.0 / 5.0) + 32.0;//kenapa dibuat desimal? karena jika tidak dibuat desimal 
    //maka hasilnya akan dibulatkan ke bawah, sehingga hasilnya tidak akurat
    cout << celsius << " derajat Celcius = " << fahrenheit << " derajat Fahrenheit" << endl;
    return 0;
} 

