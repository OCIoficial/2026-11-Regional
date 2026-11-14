// Solo actualiza el máximo cuando encuentra un '1', olvidando actualizar al
// terminar la cadena (falla cuando el bloque más largo llega hasta el final).
// @ocimatic::expected [st1=WA]
#include <bits/stdc++.h>
using namespace std;

int main() {
  cin.tie(0)->sync_with_stdio(0);

  string s;
  cin >> s;

  int actual = 0, mejor = 0;
  for (char c : s) {
    if (c == '0') {
      actual++;
    } else {
      mejor = max(mejor, actual);
      actual = 0;
    }
  }

  cout << mejor << '\n';
  return 0;
}
