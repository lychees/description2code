#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define LL long long int
#define Mod 1000000007
#define sz(v) ((int)(v).size())
#define abs(x) ((x) > 0 ? (x) : -(x))
#define clr(a,n) memset(a,n,sizeof(a))
#define FOR(i,a,n) for(int i=a;i<n;i++)
#define fastio ios::sync_with_stdio(false)
#define REVFOR(i,a,n) for(int i=a;i>n;i--)
#define FOREACH(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)
using namespace std;
typedef vector <int> V;
typedef pair <int,int> P;
typedef pair< int, P > Pi;
typedef map <string,int> M;
typedef stack <long int> S;
typedef priority_queue < Pi > PQ;
int A[100005];

int root(int u)
{
	while(A[u]!=u)
		u=A[u];
	return u;
}

int main()
{
	fastio;
	int n,ct,t,m,a,b;	LL c;	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>n>>m;	PQ pq;	LL val=1;
		FOR(i,0,n+1)	A[i]=i;
		FOR(i,0,m)
		{
			cin>>a>>b>>c;
			pq.push(mp(-c,mp(a,b)));
		}
		FOR(i,0,m)
		{
			Pi q=pq.top();	pq.pop();
			int x=q.second.first;		int y=q.second.second;	LL temp=(-(q.first));
			int r_x=root(x);	int r_y=root(y);
			if (r_x==r_y)	continue;
			A[r_x]=r_y;
			val=(val*(temp))%Mod;
		}
		cout<<val<<'\n';
	}
	return 0;	
}
