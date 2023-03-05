#include <iostream>
using namespace std;
template <typename T>
void Swap(T &a, T &b);
int main()
{
    char a, b;
    cin >> a >> b;
    Swap(a, b);
    cout << a << " " << b << endl;
}
template <typename T>
void Swap(T &a, T &b)
{
    T c = a;
    a = b;
    b = c;
}