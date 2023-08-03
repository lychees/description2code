#include <bits/stdc++.h>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	int t;
	long n;
	cin>>t;
	
	while(t--)
	{
		cin>>n;
		long int happ[n],ang[n],sum[n],asum=0,i;
		memset(sum,0,n*sizeof(long));
		
		for(i=0;i<n;i++)
		{
			cin>>happ[i]>>ang[i];
			sum[i]=sum[i]+happ[i]+ang[i];
			asum+=ang[i];
		}
		
		sort(sum,sum+n);
		cout<<(sum[n-2]+sum[n-1]-asum)<<endl;
		
	}
}
