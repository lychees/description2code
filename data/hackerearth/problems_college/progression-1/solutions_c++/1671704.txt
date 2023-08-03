#include <iostream>
using namespace std;
int a[100000]={0};
int main()
{
	int n,i,p,j;
    cin>>n;
    for(i=0;i<=100;i++)
    {
    	for(j=0;j<=100;j++)
    	{
    		a[45*i+6*j]=1;
    	//	a[51*i+6*j]=1;
    		
    	}
    	
    }
    
    while(n--)
    {
    	cin>>p;
    	if(a[p]==1 && p>=45 && p<=500)
    	cout<<"CORRECT"<<endl;
    	else
    	cout<<"INCORRECT"<<endl;
    	
    	
    	
    }
    
    
    
    return 0;
}
