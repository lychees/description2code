#include <iostream>
#include <cmath>
using namespace std;

long long count = 0;

void splice (long long a, long long b) {
	if (a == b == 1) return;
	if (b != 1) {
		count +=  a/b;
		splice (b, a%b);
	}
	else {
		count += a-b;
	}
	return;
}
	
int main() {
	int t;
	cin >> t;
	
	while (t--) {
		long long a,b;
		cin >> a >> b;
		if (b > a) {
			long long temp = a;
			a = b;
			b = temp;
		}
		splice(a,b);
		cout << count << endl;
		count = 0;
	}
}
