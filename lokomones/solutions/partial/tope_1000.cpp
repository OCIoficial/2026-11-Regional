// Simula hasta un tope fijo de 1000 rondas (suficiente para la subtarea 1
// donde H <= 1000, pero insuficiente en la subtarea 2).
// @ocimatic::expected [st1=OK, st2=WA]
#include <bits/stdc++.h>
using namespace std;

int main() {
  cin.tie(0)->sync_with_stdio(0);

  int k;
  cin >> k;
  vector<vector<int64_t>> p(k + 1, vector<int64_t>(k + 1));
  for (int i = 1; i <= k; i++) {
    for (int j = 1; j <= k; j++) {
      cin >> p[i][j];
    }
  }

  int64_t h, a;
  int t;
  cin >> h >> a >> t;

  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    int64_t hi, ai;
    int ti;
    cin >> hi >> ai >> ti;

    int64_t vida_v = h;
    int64_t vida_i = hi;
    for (int ronda = 0; ronda < 1000 && vida_v > 0 && vida_i > 0; ronda++) {
      vida_i -= a * p[t][ti];
      if (vida_i <= 0) break;
      vida_v -= ai * p[ti][t];
    }

    if (vida_v <= 0 && vida_i > 0) {
      cout << i << '\n';
      return 0;
    }
  }

  cout << -1 << '\n';
  return 0;
}
