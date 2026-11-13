// Solo verifica que las poleras no usadas sean subsecuencia de C, olvidando
// comparar los colores de las poleras usadas.
// @ocimatic::expected [st1=WA, st2=WA, st3=WA, st4=WA]
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
  for (int x : c) {
    if (pos < n - k && x == d[pos]) pos++;
  }

  cout << (pos == n - k ? "SI" : "NO") << '\n';
  return 0;
}
