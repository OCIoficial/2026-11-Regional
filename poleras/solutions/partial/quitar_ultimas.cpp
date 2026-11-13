// Greedy incorrecto: saca de C las poleras del final de D eligiendo siempre la
// última aparición de cada color, y compara lo que queda con el inicio de D.
// Falla, por ejemplo, con C = 1 2 1, K = 1, D = 2 1 1.
// @ocimatic::expected [st1=OK, st2=WA, st3=WA]
#include <bits/stdc++.h>
using namespace std;

int main() {
  cin.tie(0)->sync_with_stdio(0);

  int n, k;
  cin >> n >> k;
  vector<int> c(n), d(n);
  for (int &x : c) cin >> x;
  for (int &x : d) cin >> x;

  vector<int> resta(n + 1, 0);
  for (int i = n - k; i < n; i++) resta[d[i]]++;

  vector<int> quedan;
  for (int i = n - 1; i >= 0; i--) {
    if (resta[c[i]] > 0) {
      resta[c[i]]--;
    } else {
      quedan.push_back(c[i]);
    }
  }
  reverse(quedan.begin(), quedan.end());

  bool ok = quedan == vector<int>(d.begin(), d.begin() + (n - k));
  cout << (ok ? "SI" : "NO") << '\n';
  return 0;
}
