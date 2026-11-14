// Usa enteros de 32 bits (int) y multiplica turnos_i * dano_v para comparar
// contra H_i. En la subtarea 1 (H <= 1000) no hay desbordamiento, pero en la
// subtarea 2 (H <= 10^9) desborda int de 32 bits.
// @ocimatic::expected [st1=OK, st2=WA]
#include <bits/stdc++.h>
using namespace std;

int main() {
  cin.tie(0)->sync_with_stdio(0);

  int k;
  cin >> k;
  vector<vector<int>> p(k + 1, vector<int>(k + 1));
  for (int i = 1; i <= k; i++) {
    for (int j = 1; j <= k; j++) {
      cin >> p[i][j];
    }
  }

  int h, a, t;
  cin >> h >> a >> t;

  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    int hi, ai, ti;
    cin >> hi >> ai >> ti;

    int dano_v = a * p[t][ti];
    int dano_i = ai * p[ti][t];

    int turnos_i = (h + dano_i - 1) / dano_i;
    // Para sobrevivir los primeros turnos_i ataques de Vichochú se requiere
    // hi > turnos_i * dano_v, pero en 32 bits este producto se desborda.
    if (turnos_i * dano_v < hi) {
      cout << i << '\n';
      return 0;
    }
  }

  cout << -1 << '\n';
  return 0;
}
