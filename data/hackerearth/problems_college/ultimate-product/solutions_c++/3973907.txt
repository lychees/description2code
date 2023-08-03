#include<bits/stdc++.h>
using namespace std;

long long int fact[100001];
vector <long long int> G[100001];
long long int comp[100001]={0};
long long int visited[100001]={0};

int ind=0;

void pre()
{
	int i;
	fact[0]=1;	
	fact[1]=1;
	for(i=2;i<100001;i++)
	fact[i]=(fact[i-1]*i)%1000000007;
}

void calc(int p)
{
	int i;
	comp[ind]++;

	visited[p]=1;
	for(i=0;i<G[p].size();i++)
	{
		if(!visited[G[p][i]])
			calc(G[p][i]);
	}
	
}


int main()
{
	pre();
	int n,k,i,j,a,b;
	cin>>n;
	cin>>k;
	for(i=0;i<k;i++)
	{
		cin>>a;
		cin>>b;
		G[a].push_back(b);
		G[b].push_back(a);
		
	}
	

	for(i=0;i<n;i++)
	{
		if(!visited[i])
		calc(i);
		
	
		ind++;
	}
	long long int ans=1;
	
	for(i=0;i<n;i++)
	{
		ans=(ans*fact[comp[i]])%1000000007;
	}
	
	cout<<ans<<endl;
	
return 0;	
}
