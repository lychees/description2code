#include <bits/stdc++.h>
#define fast ios_base::sync_with_stdio(false);cin.tie(NULL)
#define endl '\n'
 
using namespace std;
 
int main() {
	fast;
	int t, index, n;
	cin >> t;
	
	while (t--) {
		cin >> index >> n;
		if (index == 0 or index == 2) { 
			if (n == 0 and index == 2) cout << "2" << endl;
			else if (n & 1) 		   cout << "1" << endl; 
			else            		   cout << "0" << endl; 
		}
		if (index == 1) {
			if (n & 1) cout << "0" << endl; 
			else       cout << "1" << endl; 
		}	
	}
	return 0;
}