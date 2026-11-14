// Supone que Emilia se acuesta en el primer tramo sin ronquidos disponible y
// devuelve el largo de ese primer bloque de '0's.
// @ocimatic::expected [st1=WA]
#include <bits/stdc++.h>
using namespace std;

int main() {
  cin.tie(0)->sync_with_stdio(0);

  string s;
  cin >> s;

  int i = 0;
  while (i < (int)s.size() && s[i] == '1') i++;
  int ans = 0;
  while (i < (int)s.size() && s[i] == '0') {
    ans++;
    i++;
  }

  cout << ans << '\n';
  return 0;
}
