#include<bits/stdc++.h>
using namespace std;
#define ll long long int 
vector<int> a(50000),d(50000,0);
vector< pair<int,int> > b(50000);

int main()
{
	ll n,i,j,t;
	ll p,c,m;
	scanf("%lld",&t);
	while(t--)
	{
		scanf("%lld",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			b[i].first=a[i];
			b[i].second=i;
			d[i]=0;
		}
		sort(b.begin(),b.begin()+n);
		j=n-1;
		m=0;
		p=0;
		c=0;
		for(i=0;i<n;i++)
		{
			if(a[i]==b[j].first)
			{
				d[i]=1;
				while(d[b[j].second]==1 && j>=0)
					j--;
				p+=((a[i]*m)-c);
				m=0;
				c=0;
			}
			else
			{
				m++;
				c+=a[i];
				d[i]=1;
			}
		}
		printf("%lld\n",p);
	}
	return 0;
}





	
