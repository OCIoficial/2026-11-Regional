// El costo mínimo es max(x) + N - 1: Lonk avanza de izquierda a derecha hasta
// x_i - 1 y dispara a x_i a distancia 1 (dejando libre x_i para poder pisarla
// si el siguiente meblin está en x_i + 1).
#include <bits/stdc++.h>
using namespace std;

int main() {
  cin.tie(0)->sync_with_stdio(0);

  int n;
  int64_t e;
  cin >> n >> e;

  int64_t mx = 0;
  for (int i = 0; i < n; i++) {
    int64_t x;
    cin >> x;
    mx = max(mx, x);
  }

  cout << (mx + n - 1 <= e ? "SI" : "NO") << '\n';
  return 0;
}
