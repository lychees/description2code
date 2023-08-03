#include <iostream>
using namespace std;

int main()
{
	long long int t,n,temp,sum,i,m;
    cin>>t;
    while(t--)
    {
    	cin>>n;
    	sum=0;
    	for(i=0;i<n;i++)
    	{
    		cin>>temp;
    		sum=sum+temp;
    		
    		
    	}
    	m=sum%n;
    	if(m==0)
    	cout<<"YES"<<endl;
    	else
    	cout<<"NO"<<endl;
    	
    	cout<<sum/n<<" "<<m<<endl;
    	
    }
    
    
    return 0;
}
