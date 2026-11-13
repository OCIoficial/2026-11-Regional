// Supone K = 1: busca la primera posición donde C y D difieren y verifica que
// esa polera sea la que quedó al final.
// @ocimatic::expected [st1=WA, st2=OK, st3=WA]
#include <bits/stdc++.h>
using namespace std;

int main() {
  cin.tie(0)->sync_with_stdio(0);

  int n, k;
  cin >> n >> k;
  vector<int> c(n), d(n);
  for (int &x : c) cin >> x;
  for (int &x : d) cin >> x;

  int i = 0;
  while (i < n && c[i] == d[i]) i++;
  if (i == n) {
    cout << "SI\n";
    return 0;
  }

  bool ok = c[i] == d[n - 1];
  for (int j = i + 1; j < n; j++) {
    if (c[j] != d[j - 1]) ok = false;
  }

  cout << (ok ? "SI" : "NO") << '\n';
  return 0;
}
