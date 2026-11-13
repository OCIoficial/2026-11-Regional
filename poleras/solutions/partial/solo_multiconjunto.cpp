// Solo compara los colores de C y D. Correcto cuando K = N, porque las
// poleras se pueden reordenar como se quiera.
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

  sort(c.begin(), c.end());
  sort(d.begin(), d.end());

  cout << (c == d ? "SI" : "NO") << '\n';
  return 0;
}
