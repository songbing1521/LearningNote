#include <cstdio>
#include <iostream>
using namespace std;
int main() {
  double m, n;
  cin >> m >> n;
  printf("%.2lf\n", (m * n) / (m + n));
}