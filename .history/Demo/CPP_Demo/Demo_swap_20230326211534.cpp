#include<iostream>
using namespace std;
void swap(int &a, int& b){
    a = a + b;
    b = a - b;
    a = a - b;
}
void swap(int &a, int &b){
    int t = a;
    a = b;
    b = t;
}
int main(){
    int a , b;
    cin >> a >> b;
    swap(a,b);
    cout << a << " " << b << endl;
}