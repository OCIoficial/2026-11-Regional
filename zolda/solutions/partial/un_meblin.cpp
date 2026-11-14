// Supone N = 1 (o ignora el costo de los disparos intermedios) y solo revisa
// si max(x) <= E.
// @ocimatic::expected [st1=OK, st2=WA, st3=WA]
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

  cout << (mx <= e ? "YES" : "NO") << '\n';
  return 0;
}
