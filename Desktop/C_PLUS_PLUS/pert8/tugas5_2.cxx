#include<iostream>
using namespace std;
int main(){
    int a, b, c;
    cout<<"Nama: Meishella Noer Alysia"<<endl;
    cout<<"Kelas: 01TPLP013"<<endl;
    cout<<"============================"<<endl;
    cout<<"Masukan Nilai ke-1 : "; cin>>a;
    cout<<"Masukan Nilai ke-2 : "; cin>>b;
    cout<<"Masukan Nilai ke-3 : "; cin>>c;
    if(a<b)
        if(b<c)
            cout<<"\nUrutan Nilai Dari yang Terkecil :"<<a<<" "<<b<<" "<<c<<" ";
        else
        if(a<c)
                cout<<"\nUrutan Nilai Dari yang Terkecil :"<<a<<" "<<c<<" "<<b<<" ";
            else
                cout<<"\nUrutan Nilai Dari yang Terkecil: "<<c<<" "<<a<<" "<<b<<" ";
    else
        if(a<c)
            cout<<"\nUrutan Nilai Dari yang Terkecil :"<<b<<" "<<a<<" "<<c<<" ";
        else
            if(b<c)
                cout<<"\nUrutan Nilai Dari yang Terkecil: "<<b<<" "<<c<<" "<<a<<" ";
            else
                cout<<"\nUrutan Nilai Dari yang Terkecil :"<<c<<" "<<b<<" "<<a<<" ";
}