// No reutiliza las casillas liberadas al derrotar meblins: para cada bloque de
// K meblins consecutivos, dispara a todos desde la casilla libre anterior al
// bloque gastando 1 + 2 + ... + K.
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

  sort(x.begin(), x.end());

  int64_t pos = 0;
  int64_t gasto = 0;
  int i = 0;
  while (i < n) {
    int j = i;
    while (j + 1 < n && x[j + 1] == x[j] + 1) j++;
    int64_t k = j - i + 1;
    gasto += (x[i] - 1) - pos;
    pos = x[i] - 1;
    gasto += k * (k + 1) / 2;
    i = j + 1;
  }

  cout << (gasto <= e ? "YES" : "NO") << '\n';
  return 0;
}
