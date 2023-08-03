#include <iostream>
using namespace std;
int a[41];
int main()
{
	int t,i,j,k,n;
    cin>>t;
    a[1]=1;
    a[2]=2;
    for(i=3;i<=40;i++)
    {
    	a[i]=a[i-1]+a[i-2];	
    }
    
    
    while(t--)
    {
    	cin>>n;
    	cout<<a[n]<<endl;
    	
    	
    }
    return 0;
}
