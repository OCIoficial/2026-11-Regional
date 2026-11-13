// Greedy incorrecto: saca de C las poleras del final de D eligiendo siempre la
// primera aparición de cada color, y compara lo que queda con el inicio de D.
// Falla, por ejemplo, con C = 1 2 1, K = 1, D = 1 2 1.
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
  for (int x : c) {
    if (resta[x] > 0) {
      resta[x]--;
    } else {
      quedan.push_back(x);
    }
  }

  bool ok = quedan == vector<int>(d.begin(), d.begin() + (n - k));
  cout << (ok ? "SI" : "NO") << '\n';
  return 0;
}
