#include <iostream>
using namespace std;

int main()
{
	int t,n,k,count,yes,i,j,temp;
    cin>>t;
    
    while(t--)
    {
    	cin>>n;
    	cin>>k;
    	
    	count=0;
    	yes=0;
    	
    	for(i=0;i<n;i++)
    	{
    		cin>>temp;
    		if(temp==k)
    		yes=1;
    		
    		if(temp>k)
    		count++;
    		
    		
    		
    	}
    	if(yes)
    	{
    		cout<<"YES "<<count<<endl;
    	}
    	else
    	{
    		cout<<"NO 0"<<endl;
    	}
    	
    	
    	
    }
    
    
    
    return 0;
}
