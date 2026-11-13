// Compara la suma de los colores en vez de los multiconjuntos. Correcto cuando
// K = 1, porque solo queda una polera por comparar.
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

  long long suma_c = accumulate(c.begin(), c.end(), 0LL);
  long long suma_d = accumulate(d.begin(), d.end(), 0LL);

  int pos = 0;
  for (int x : c) {
    if (pos < n - k && x == d[pos]) pos++;
  }

  cout << (suma_c == suma_d && pos == n - k ? "SI" : "NO") << '\n';
  return 0;
}
