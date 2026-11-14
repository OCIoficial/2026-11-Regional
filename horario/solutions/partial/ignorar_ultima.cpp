// Error de borde: itera solo hasta i < 9, ignorando la última hora.
// @ocimatic::expected [st1=WA]
#include <bits/stdc++.h>
using namespace std;

int main() {
  cin.tie(0)->sync_with_stdio(0);

  string s;
  cin >> s;

  int actual = 0, mejor = 0;
  for (int i = 0; i < 9; i++) {
    if (s[i] == '0') {
      actual++;
      mejor = max(mejor, actual);
    } else {
      actual = 0;
    }
  }

  cout << mejor << '\n';
  return 0;
}
