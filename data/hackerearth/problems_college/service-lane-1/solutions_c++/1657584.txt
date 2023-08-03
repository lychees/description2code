#include <iostream>
using namespace std;
int a[1000001];

int main()
{
	int n,t,l,r,i;
    cin>>n;
    cin>>t;
    for(i=0;i<n;i++)
    cin>>a[i];
    
    while(t--)
    {
    	cin>>l;
    	cin>>r;
    	int min=9999;
    	for(i=l;i<=r;i++)
    	{
    		if(min>a[i])
    		min=a[i];
    		
    	}
    	
    	cout<<min<<endl;
    	
    }
    
    
    return 0;
}
