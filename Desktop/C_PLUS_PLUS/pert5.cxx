
//pertemuan 5 pada tanggal 23 September 2026 

// int main(){
    //     int A,B,C;
    //     cout<<"Masukkan angka pertama"<<endl;
    //     cin>>A;
    //     cout<<"Masukkan angka kedua"<<endl;
    //     cin>>B;
    //     C=A+B;
    //     cout<<"hasil dari A+B adalah "<<C<<endl;
    // }
    
    //tugas 4 tanggal 23 September 2026
    //algoritma dan pemrograman dasar
    //Meishella Noer Alysia
    //01TPLP013
    //1. buatlah algoritma dan pemrograman untuk menghitung luas segitiga, tentukan:
    //a. pemecahan masalahnya
    //Untuk mencari luas segitiga, kita menggunakan rumus A*B/2. Dimana A merupakan panjang alas dari segitiga
    //dan B merupakan tinggi dari segitiga.
    //b. flowchart
    //c.listing program dan output
    //2. susunlah algoritma dan pemrograman untuk menghitung 3 buah bilangan bulat, hasil dari perkalian ketiga buah bilangan
    // bulat tersebut, tercetak dalam program, tentukan:
    //a. flowchart
    //b. listing program dan output 
    //upload hasil dari kedua soal tersebut ke dalam google drive tugas-04 dalam bentuk pdf. dengan nama file :tugas04_nama
    
#include <iostream>
using namespace std;
int main(){
    int A,B,C;
    cout<<"MENGHITUNG LUAS SEGITIGA"<<endl;
    cout<<"Masukkan panjang alas segitiga: "<<endl;
    cin>>A;
    cout<<"Masukkan tinggi segitiga: "<<endl;
    cin>>B;
    C=A*B/2;
    cout<<"LUAS SEGITIGA ADALAH: "<<C<<endl;

    int D,E,F,G;
    cout<<"OPERASI PERKALIAN 3 BILANGAN"<<endl;
    cout<<"Masukkan angka pertama: "<<endl;
    cin>>D;
    cout<<"Masukkan angka kedua: "<<endl;
    cin>>E;
    cout<<"Masukkan angka ketiga: "<<endl;
    cin>>F;
    G = D*E*F;
    cout<<"Hasil dari perkalian 3 angka adalah: "<<G<<endl;
    return 0;
}

