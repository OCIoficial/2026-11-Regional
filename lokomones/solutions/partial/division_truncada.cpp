// Usa división entera truncada (H / dano) en lugar de división techo.
// @ocimatic::expected [st1=WA, st2=WA]
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

    int64_t dano_v = a * p[t][ti];
    int64_t dano_i = ai * p[ti][t];

    int64_t turnos_v = hi / dano_v;
    int64_t turnos_i = h / dano_i;

    if (turnos_i < turnos_v) {
      cout << i << '\n';
      return 0;
    }
  }

  cout << -1 << '\n';
  return 0;
}
