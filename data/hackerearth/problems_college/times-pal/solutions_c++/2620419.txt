#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

bool isPalin(string s){
	int n=s.size();
	for(int i=0; i<n/2; i++)
		if(s[i] != s[n-1-i])
			return false;
	return true;
}


void solve(){
	string a, b;
	cin>>a>>b;
	string c;
	int m=a.size();
	int n=b.size();
	int count=0;
	for(int i=0; i<=m; i++){
        //cout<<a.substr(0, i)<<" "<<b<<" "<<a.substr(i, m-i);
		c=a.substr(0,i) + b +a.substr(i, m-i);
		//cout<<c<<endl;
		if(isPalin(c))
			count++;
	}
	cout<<count<<endl;
}

int main()
{
    int t;
    //string a="aba";
    //string b="b";
    //string c=a.substr(0,0)+b+a.substr(0,a.size());
    //out<<c<<" here"<<endl;
    cin>>t;
    while(t--)
    	solve();
    return 0;
}
