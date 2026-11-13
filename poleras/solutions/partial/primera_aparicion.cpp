// Greedy incorrecto: compara los colores y luego revisa que la primera
// aparición en C de cada polera no usada vaya creciendo. Funciona si los
// colores son distintos, pero falla con repetidos, por ejemplo con
// C = 1 2 1 3, K = 1, D = 2 1 3 1.
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

  vector<int> cnt(n + 1, 0);
  for (int x : c) cnt[x]++;
  for (int x : d) cnt[x]--;
  for (int x = 1; x <= n; x++) {
    if (cnt[x] != 0) {
      cout << "NO\n";
      return 0;
    }
  }

  vector<int> primera(n + 1, -1);
  for (int i = 0; i < n; i++) {
    if (primera[c[i]] == -1) primera[c[i]] = i;
  }

  bool ok = true;
  for (int i = 1; i < n - k; i++) {
    if (primera[d[i - 1]] >= primera[d[i]]) ok = false;
  }

  cout << (ok ? "SI" : "NO") << '\n';
  return 0;
}
