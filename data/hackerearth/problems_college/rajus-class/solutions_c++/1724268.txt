#include <bits/stdc++.h>
using namespace std;
int a[101];
int main()
{
	int t,i,j,k,temp,n,r;
	string s[101],temp1;
	
   cin>>t;
   while(t--)
   {
   	cin>>n;
   	
   	for(i=0;i<n;i++)
   	{
   		cin>>a[i];
   		cin>>s[i];
   	
   	}
   	
   	
   	for(i=0;i<n;i++)
   	{
   		for(j=i+1;j<n;j++)
   		{
   			if(a[i]>a[j])
   			{
   				temp=a[i];
   				a[i]=a[j];
   				a[j]=temp;
   				
   				
   				temp1=s[i];
   				s[i]=s[j];
   				s[j]=temp1;
   				
   				
   				
   				
   			}
   			
   			
   			
   			
   		}
   		
   		
   		
   	}
   	
   	cin>>r;
   	cout<<s[r-1]<<endl;
   	
   	
   	
   }
    return 0;
}
