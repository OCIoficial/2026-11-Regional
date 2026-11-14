// Ignora la tabla de efectividad de tipos P y usa directamente el ataque base.
// @ocimatic::expected [st1=WA, st2=WA]
#include <bits/stdc++.h>
using namespace std;

int main() {
  cin.tie(0)->sync_with_stdio(0);

  int k;
  cin >> k;
  for (int i = 0; i < k * k; i++) {
    int x;
    cin >> x;
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

    int64_t turnos_v = (hi + a - 1) / a;
    int64_t turnos_i = (h + ai - 1) / ai;

    if (turnos_i < turnos_v) {
      cout << i << '\n';
      return 0;
    }
  }

  cout << -1 << '\n';
  return 0;
}
