// Nunca salta: dispara a todos los meblins desde la posición 0.
// @ocimatic::expected [st1=OK, st2=WA, st3=WA]
#include <bits/stdc++.h>
using namespace std;

int main() {
  cin.tie(0)->sync_with_stdio(0);

  int n;
  int64_t e;
  cin >> n >> e;

  int64_t suma = 0;
  for (int i = 0; i < n; i++) {
    int64_t x;
    cin >> x;
    suma += x;
  }

  cout << (suma <= e ? "SI" : "NO") << '\n';
  return 0;
}
