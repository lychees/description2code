#include <iostream>
using namespace std;

int main()
{
	long long int a[100000],i,t,num;
    cin>>t;
    a[0]=1;
    a[1]=1;
    for(i=2;i<=90;i++)
    {
    	a[i]=a[i-1]+a[i-2];
    }
    
    
    while(t--)
    {
    	cin>>num;
    	if(num>2)
    	cout<<a[num-2]<<" "<<a[num-1]<<endl;
    	else if(num==1)
    	cout<<"0"<<" 1"<<endl;
    	else if(num==2)
    	cout<<"1"<<" 1"<<endl;
    	
    }
    
    
    return 0;
}
