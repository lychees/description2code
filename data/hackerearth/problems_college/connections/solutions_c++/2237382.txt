#include <bits/stdc++.h>
using namespace std;
vector<int> V[100005];
int Vis[100005],val=1;
void dfs(int i)
{
	Vis[i]=val;
	for( int j=0;j<V[i].size();j++)
	{
		int q=V[i][j];
		if(!Vis[q])	dfs(q);
	}
}
int dcd(int A,int B)
{
	for(int i=0;i<V[A].size();i++)
	{
		if(V[A][i]==B)
			return 1;
	}
	if(Vis[A]==Vis[B])
		return 2;
	return 3;
}
int main()
{
	int T,N,M,A,B,Q;
	scanf("%d %d",&N,&M);
	for(int i=1;i<=N;i++)
	{
		V[i].clear();
	}
	memset(Vis,0,sizeof(Vis));
	while(M--)
	{
		scanf("%d %d",&A,&B);
		V[A].push_back(B);
		V[B].push_back(A);
	}
	val=1;
	for(int i=1;i<=N;i++)
	{
		if(!Vis[i])
		{
			dfs(i);	val++;
		}
	}
	scanf("%d",&Q);
	for(int i=0;i<Q;i++)
	{
		scanf("%d %d",&A,&B);
		int val=dcd(A,B);
		switch(val)
		{
			case 1:cout<<"Direct Connection"<<'\n';	break;
			case 2:cout<<"Indirect Connection"<<'\n';	break;
			case 3:cout<<"No Connection"<<'\n';	break;
		}
	}
return 0;
}
