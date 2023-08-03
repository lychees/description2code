#include <bits/stdc++.h>
#define fast ios_base::sync_with_stdio(false);cin.tie(NULL)

using namespace std;

bool isEven(char c){
	if((c - '0') & 1)
		return false;
	return true;
}

void solve(vector<int> &even, string &s){
	for(int i = 0; i < s.size(); i++) 
		if(isEven(s[i]))
			even[i + 1]++;
	
	for(int i = 1; i < even.size(); i++)
		even[i] += even[i - 1];
}

int main(){
	fast;
	string s;
	cin >> s;
	vector<int> even(s.size() + 1, 0);
	solve(even, s);
	for(int i = 1; i < even.size(); i++) {
		if(i > 1)
			cout << " ";
		cout << even[s.size()] - even[i - 1];

	}
	cout << endl;
	return 0;
}