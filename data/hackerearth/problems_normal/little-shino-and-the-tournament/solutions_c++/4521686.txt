#include<bits/stdc++.h>
#define fast ios_base::sync_with_stdio(0);cin.tie(0)
#define mod 1000000007
#define F first
#define S second
typedef long long ll;
using namespace std;

pair<long long int, int> a[100005];
int answer[100005]={0};

int main() 
{
	int n,q;
	long long int temp;
	scanf("%d %d",&n,&q);
    
    for(int i = 1; i<=n; i++)
    {
		scanf("%lld",&temp);
		a[i].F = temp;
		a[i].S = i;
    }
    	
    int count = n;
    
    while(count!=1)
    {
    	int p = 1;
    	// printf("%d\n",count);
    	// for(int i = 1; i<=n; i++)
    	// printf("%d ",answer[i]);
    	
    	// printf("\n");
    	
    	// for(int i = 1; i<=n; i++)
    	// printf("%d ",a[i].F);
    	
    	// printf("\n");
    	
    	// for(int i = 1; i<=n; i++)
    	// printf("%d ",a[i].S);
    	
    	// printf("\n\n");
    	
    	
    	
    	for(int i = 1; i<count; i+=2)
    	{	
    	    answer[a[i].S]++;
    		answer[a[i+1].S]++;
    
    		if(a[i].F>a[i+1].F)
    		{
    			a[p].F = a[i].F;
    			a[p].S = a[i].S;
    			p++;
    		}
    		
    		else if(a[i+1].F>a[i].F)
    		{
    			a[p].F = a[i+1].F;
    			a[p].S = a[i+1].S;
    			p++;
    			
    			// if(count==2)
    			// {
    			// 	printf("am here\n");
    			// 	for(int i = 1; i<=n; i++)
    			// 	printf("%d ",a[i]);
    			// 	cout<<endl;
    			// }
    		}
    		
    		// if(count == 2)
    		// {
    	 //    for(int i = 1; i<=n; i++)
    	 //    printf("%d ",answer[i]);
    	     
    	     
    	 //    cout<<endl<<a[1].F<<endl;
    	 //    cout<<endl;
    		// }
    		
    	}
    	
    	if(count%2==1)
    	{
    		a[(count/2) + 1].F = a[count].F;
    		a[(count/2) + 1].S = a[count].S;
    		count = (count/2) + 1;
    	}
    	
    	else if(count%2==0)
    	{
    		count = count/2;
    	}
    	
    	
    }
    	
    	
    for(int j = 1; j<=q; j++)
    {
    	int temp;
    	scanf("%d",&temp);
    	printf("%d\n",answer[temp]);
    	
    }
    
	return 0;
}
