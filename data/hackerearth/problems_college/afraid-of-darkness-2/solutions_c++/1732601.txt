#include <iostream>
#include<algorithm>
using namespace std;
long long int a[1000001];
int main()
{
	int t,m,i,j,k,n;
    cin>>t;
    while(t--)
    {
    	cin>>m;
    	for(i=0;i<m;i++)
    	cin>>a[i];
    	
    	sort(a,a+m);
    	int count=0,key=0;
    	if(m==0)
    	cout<<"0"<<endl;
    	
    	else
    	{
    	while(1)
    	{
    		
    		for(i=(m-1);i>=(m-count-1);i--)
    		{
    			if(a[i]==0)
    			key=1;
    			
    			a[i]--;
    		
    			
    		}
    		
    		if(!key)
    		count++;
    		else
    		break;
    		
    		if(count==m)
    		break;
    		
    		sort(a,a+m);
    		
    	}
    	
    	cout<<count<<endl;
    	}
    }
    return 0;
}
