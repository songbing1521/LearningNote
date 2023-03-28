#include<iostream>
using namespace std;
void swap(int x, int y){//  x = a, y = b;
    x = x + y;
    y = x - y;
    x = x - y;
}
// void swap(int &a, int &b){
//     int t = a;
//     a = b;
//     b = t;
// }
int main(){
    int a , b;
    cin >> a >> b;
    swap(a,b);
    cout << a << " " << b << endl;
}