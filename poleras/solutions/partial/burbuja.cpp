// Solución correcta, pero compara los colores ordenando con bubble sort en
// O(N^2).
// @ocimatic::expected [st1=TLE, st2=TLE, st3=OK, st4=TLE]
#include <bits/stdc++.h>
using namespace std;

void burbuja(vector<int> &v) {
  int n = v.size();
  for (int i = 0; i < n; i++) {
    for (int j = 0; j + 1 < n - i; j++) {
      if (v[j] > v[j + 1]) swap(v[j], v[j + 1]);
    }
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);

  int n, k;
  cin >> n >> k;
  vector<int> c(n), d(n);
  for (int &x : c) cin >> x;
  for (int &x : d) cin >> x;

  vector<int> sc = c, sd = d;
  burbuja(sc);
  burbuja(sd);
  if (sc != sd) {
    cout << "NO\n";
    return 0;
  }

  int pos = 0;
  for (int x : c) {
    if (pos < n - k && x == d[pos]) pos++;
  }

  cout << (pos == n - k ? "SI" : "NO") << '\n';
  return 0;
}
