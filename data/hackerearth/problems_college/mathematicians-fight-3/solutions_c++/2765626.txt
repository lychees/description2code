#include<bits/stdc++.h>
#define len 1000005
#define Mod 1000000007
#define For(i,a,b) for(ll i=a;i<b;i++)
using namespace std;
typedef double ll;
ll arr[len];
int main(){
ll t;
cin>>t;
while(t--){
	ll n;
	cin>>n;
	ll ans=2*(n-pow(2,floor(log2(n))))+1;
	cout<<long(ans)<<"\n";
}
}
