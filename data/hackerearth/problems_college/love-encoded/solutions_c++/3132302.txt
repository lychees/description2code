#include <bits/stdc++.h>
#define fast ios_base::sync_with_stdio(false);cin.tie(NULL)
#define endl '\n'

using namespace std;

int main() {
  fast;
  int t, k;
  string s, alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  cin >> t;

  while (t--) {
    cin >> k >> s;
    for (int i = 0; i < s.size(); i++) {
      s[i] = alph[((s[i] - 'A') - k + 26) % 26];
    }
    cout << s << endl;
  }
  return 0;
}
