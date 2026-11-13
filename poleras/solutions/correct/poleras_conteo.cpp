// Igual que poleras_fullscore.cpp, pero compara los colores con un arreglo de
// conteo en lugar de un map.
#include <bits/stdc++.h>
using namespace std;

int main() {
  cin.tie(0)->sync_with_stdio(0);

  int n, k;
  cin >> n >> k;
  vector<int> c(n), d(n);
  for (int &x : c) cin >> x;
  for (int &x : d) cin >> x;

  vector<int> cnt(n + 1, 0);
  for (int x : c) cnt[x]++;
  for (int x : d) cnt[x]--;
  for (int x = 1; x <= n; x++) {
    if (cnt[x] != 0) {
      cout << "NO\n";
      return 0;
    }
  }

  int pos = 0;
  for (int i = 0; i < n && pos < n - k; i++) {
    if (c[i] == d[pos]) pos++;
  }

  cout << (pos == n - k ? "SI" : "NO") << '\n';
  return 0;
}
