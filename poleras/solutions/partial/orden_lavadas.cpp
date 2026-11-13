// Supone que las poleras usadas también conservan su orden relativo al
// ponerse al final. Correcto cuando K = 1.
// @ocimatic::expected [st1=WA, st2=OK, st3=WA, st4=WA]
#include <bits/stdc++.h>
using namespace std;

int main() {
  cin.tie(0)->sync_with_stdio(0);

  int n, k;
  cin >> n >> k;
  vector<int> c(n), d(n);
  for (int &x : c) cin >> x;
  for (int &x : d) cin >> x;

  int pos = 0;
  vector<int> lavadas;
  for (int x : c) {
    if (pos < n - k && x == d[pos]) {
      pos++;
    } else {
      lavadas.push_back(x);
    }
  }

  bool ok = pos == n - k && equal(lavadas.begin(), lavadas.end(), d.begin() + (n - k));
  cout << (ok ? "SI" : "NO") << '\n';
  return 0;
}
