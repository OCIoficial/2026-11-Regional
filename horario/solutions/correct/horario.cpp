// Recorre la cadena llevando la cantidad actual de ceros consecutivos y el
// máximo visto hasta el momento.
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
      mejor = max(mejor, actual);
    } else {
      actual = 0;
    }
  }

  cout << mejor << '\n';
  return 0;
}
