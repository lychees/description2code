/*
ID: ashish1610
PROG:
LANG: C++
*/
#include<bits/stdc++.h>
using namespace std;
#define ll				long long int
#define vi				vector<int>
#define vl				vector<ll>
#define	pii				pair<int,int>
#define pil				pair<int, ll>
#define pll				pair<ll, ll>
#define pli 			pair<ll, int>
#define pb(v, a)		v.push_back(a)
#define mp(a, b)		make_pair(a, b)
#define MOD				1000000007
#define rep(i, a, b)	for(i=a; i<=b; ++i)
#define rrep(i, a, b)	for(i=a; i>=b; --i)
#define si(a)			scanf("%d", &a)
#define sl(a)			scanf("%I64d", &a)
#define pi(a)			printf("%d", a)
#define pl(a)			printf("%I64d", a)
#define pn 				printf("\n")
ll pow_mod(ll a, ll b)
{
	ll res = 1;
	while(b)
	{
		if(b & 1)
			res = (res * a) % MOD;
		a = (a * a) % MOD;
		b >>= 1;
	}
	return res;
}
bool visited[1000005];
int cst[4];
int bfs(int n, int m)
{
	memset(visited, false, sizeof(visited));
	queue<pair<int, int> > q;
	q.push(mp(n, 0));
	int cnt = 0;
	while(!q.empty())
	{
		pair<int, int> tmp = q.front();
		q.pop();
		if(tmp.first == m)
		{
			return tmp.second;
		}
		if(visited[tmp.first])
			continue;
		visited[tmp.first] = true;
		if(tmp.first - cst[3] >= 2)
		{
			if(!visited[tmp.first - cst[3]])
				q.push(mp(tmp.first - cst[3], tmp.second + 1));
		}
		if(cst[0] * tmp.first <= 1000000)
		{
			if(!visited[tmp.first * cst[0]])
				q.push(mp(cst[0] * tmp.first, tmp.second + 1));
		}
		if(tmp.first + cst[2] <= 1000000)
		{
			if(!visited[tmp.first + cst[2]])
				q.push(mp(tmp.first + cst[2], tmp.second + 1));
		}
		if(tmp.first / cst[1] >= 2)
		{
			if(!visited[tmp.first / cst[1]])
				q.push(mp(tmp.first / cst[1], tmp.second + 1));
		}
	}
	return -1;
}
int main()
{
	int t;
	si(t);
	while(t--)
	{
		int n, m;
		si(n);
		si(m);
		si(cst[0]);
		si(cst[1]);
		si(cst[2]);
		si(cst[3]);
		if(n == m)
			printf("0\n");
		else if(cst[0] == 1 && cst[1] == 1 && cst[2] == 0 && cst[3] == 0)
			printf("-1\n");
		else
		{
			pi(bfs(n, m));
			pn;
		}
	}
	return 0;
}