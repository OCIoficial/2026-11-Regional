// Supone que la entrada viene ordenada de menor a mayor y toma x[n - 1] como
// la posición más lejana sin ordenar ni buscar el máximo.
// @ocimatic::expected [st1=OK, st2=WA, st3=WA]
#include <bits/stdc++.h>
using namespace std;

int main() {
  cin.tie(0)->sync_with_stdio(0);

  int n;
  int64_t e;
  cin >> n >> e;
  vector<int64_t> x(n);
  for (int64_t &v : x) cin >> v;

  cout << (x.back() + n - 1 <= e ? "YES" : "NO") << '\n';
  return 0;
}
