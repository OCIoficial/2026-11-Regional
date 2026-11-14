// Supone que los meblins ocupan N casillas consecutivas a partir de min(x),
// por lo que max(x) = min(x) + N - 1 y el costo es min(x) + 2*N - 2.
// @ocimatic::expected [st1=OK, st2=OK, st3=WA]
#include <bits/stdc++.h>
using namespace std;

int main() {
  cin.tie(0)->sync_with_stdio(0);

  int n;
  int64_t e;
  cin >> n >> e;
  vector<int64_t> x(n);
  for (int64_t &v : x) cin >> v;

  int64_t mn = *min_element(x.begin(), x.end());
  cout << (mn + 2LL * n - 2 <= e ? "YES" : "NO") << '\n';
  return 0;
}
