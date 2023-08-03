#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define sz(v) ((int)(v).size())
#define abs(x) ((x) > 0 ? (x) : -(x))
#define FOREACH(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)
typedef long long LL;
typedef vector <int> V;
typedef pair <LL,LL> P;

int main()
{
	ios::sync_with_stdio(false);
	int t;	cin>>t;	LL m,n,a,b,i;
	while(t--)
	{
		cin>>n>>m;	P p[n];
		for(i=0;i<n;i++)
		{
			cin>>a>>b;
			p[i]=mp(b,-a);
		}
		sort(p,p+n);
		for(i=0;i<n;i++)
		{
			if(m<p[i].first)
				break;
			else
				m+=-p[i].second;
		}
		if(i<n)
			cout<<"NO"<<'\n';
		else
			cout<<"YES"<<'\n';
		
	}
	return 0;
}
