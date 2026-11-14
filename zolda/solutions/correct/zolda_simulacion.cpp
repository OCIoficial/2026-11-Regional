// Ordena las posiciones de los meblins y simula la estrategia óptima de saltar
// a x_i - 1 y disparar a distancia 1 de izquierda a derecha.
#include <bits/stdc++.h>
using namespace std;

int main() {
  cin.tie(0)->sync_with_stdio(0);

  int n;
  int64_t e;
  cin >> n >> e;
  vector<int64_t> x(n);
  for (int64_t &v : x) cin >> v;

  sort(x.begin(), x.end());

  int64_t pos = 0;
  int64_t gasto = 0;
  for (int64_t m : x) {
    gasto += (m - 1) - pos;
    pos = m - 1;
    gasto += 1;
  }

  cout << (gasto <= e ? "YES" : "NO") << '\n';
  return 0;
}
