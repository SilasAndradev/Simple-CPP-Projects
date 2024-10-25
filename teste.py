#include <iostream>
#include <locale.h>
using namespace std;

int main(){
    setlocale(LC_ALL, "Portuguese_Brazil");
    int num, maior = 0, menor = 9999999;

    for(int cont = 1; cont < 5; cont++){
       cout<<"Digite um número: "<<endl;
       cin>>num;

       if(num > maior){
        maior = num;
       } 

       if (num < menor){
        menor = num;
       }

    }
    cout<<"O maior número é: "<<maior;
    cout<<"O menor número é: "<<menor;
    
}
