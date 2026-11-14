// Simula la batalla turno por turno restando vida en un ciclo while.
// Pasa la subtarea 1 (H <= 1000), pero excede el límite de tiempo en la
// subtarea 2 cuando la vida es 10^9 y el daño es 1.
// @ocimatic::expected [st1=OK, st2=TLE]
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
    int turno = 0;

    while (vida_v > 0 && vida_i > 0) {
      if (turno % 2 == 0) {
        vida_i -= a * p[t][ti];
      } else {
        vida_v -= ai * p[ti][t];
      }
      turno++;
    }

    if (vida_i > 0) {
      cout << i << '\n';
      return 0;
    }
  }

  cout << -1 << '\n';
  return 0;
}
