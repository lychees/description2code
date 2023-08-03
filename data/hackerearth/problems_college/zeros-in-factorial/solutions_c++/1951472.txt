#include <iostream>
#include<algorithm>

using namespace std;
typedef long long ll;
ll arr[1000001];
void zero()
{
	arr[0]=0;
	arr[1]=0;
	ll n2=0,n5=0;
	for(ll i=2;i<=1000001;i++){
		ll j = i;
   		
   		while(j%2==0){
   			n2++;
    		j=j/2;
   		}
   		while(j%5==0){
   			n5++;
   			j=j/5;
   			}
   	arr[i]=arr[i-1]+((n2<n5)?n2:n5);
	}
}
int main() 
{
    int t;
    cin>>t;
    zero();
    while(t--){
    	ll a,b;
    	cin>>a>>b;
    	
    	cout<<arr[b]-arr[a-1]<<endl;
    }
  
	return 0;
}
