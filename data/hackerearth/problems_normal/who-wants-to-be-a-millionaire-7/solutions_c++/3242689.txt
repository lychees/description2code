#include <bits/stdc++.h>
#define fast ios_base::sync_with_stdio(false);cin.tie(NULL)
#define endl '\n'

using namespace std;

int main() {
  fast;
  int t;
  double n;
  cin >> t;

  while (t--) {
    cin >> n;
    cout << fixed << setprecision(6) << (n - 1) / n << endl;
  }
  return 0;
}
