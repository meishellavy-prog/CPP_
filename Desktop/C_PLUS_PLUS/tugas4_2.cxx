#include <iostream>
using namespace std;
//2. susunlah algoritma dan pemrograman untuk menghitung 3 buah bilangan bulat, hasil dari perkalian ketiga buah bilangan
    // bulat tersebut, tercetak dalam program, tentukan:
    //a. flowchart
    //b. listing program dan output 
    //upload hasil dari kedua soal tersebut ke dalam google drive tugas-04 dalam bentuk pdf. dengan nama file :tugas04_nama
int main(){
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
