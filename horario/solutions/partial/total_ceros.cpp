// Cuenta el total de horas sin ronquidos en lugar de las horas consecutivas.
// @ocimatic::expected [st1=WA]
#include <bits/stdc++.h>
using namespace std;

int main() {
  cin.tie(0)->sync_with_stdio(0);

  string s;
  cin >> s;

  cout << count(s.begin(), s.end(), '0') << '\n';
  return 0;
}
