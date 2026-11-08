#include <bits/stdc++.h>
using namespace std;

template <class T>
using vec = vector<T>;
using ll = int64_t;
using pii = array<int, 2>;
using vi = vec<int>;

#define pb push_back
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
#define rep(i,a,b) for (int i = a; i < (b); ++i)
void solve() {
    int n, k;
    cin >> n >> k;

    vi c(n), d(n);
	rep(i,0,n) cin >> c[i];
	rep(i,0,n) cin >> d[i];

    map<int,int> freq;
    for(int x: c) freq[x]++;
    for(int x: d) freq[x]--;

    for(auto [color, amount]: freq){
        if(amount != 0){
            cout << "No" << '\n';
            return;
        }
    }

    int pos = 0;
    for(int x: c){
        if(pos < n-k && x==d[pos]){
            pos++;
        }
    }

    cout << (pos == n - k ? "Si" : "No") << '\n';
}

signed main(){
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);

	int t = 1;
	//cin >> t;
	while(t--) solve();
	return 0;
}
