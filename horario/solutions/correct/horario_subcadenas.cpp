// Prueba todos los pares (i, j) y verifica si el tramo S[i..j] contiene solo
// ceros.
#include <bits/stdc++.h>
using namespace std;

int main() {
  cin.tie(0)->sync_with_stdio(0);

  string s;
  cin >> s;

  int n = s.size();
  int mejor = 0;
  for (int i = 0; i < n; i++) {
    for (int j = i; j < n; j++) {
      bool ok = true;
      for (int k = i; k <= j; k++) {
        if (s[k] != '0') ok = false;
      }
      if (ok) mejor = max(mejor, j - i + 1);
    }
  }

  cout << mejor << '\n';
  return 0;
}
