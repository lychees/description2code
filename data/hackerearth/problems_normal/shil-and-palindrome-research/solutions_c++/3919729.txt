#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll bit[26][100005];
ll n,q;
void update(ll ind,ll val,ll pos)
{
	while(ind<=n)
	{
		bit[pos][ind]+=val;
		ind+=(ind&-ind);
	}
}

ll query(ll ind,ll pos)
{
	ll ans=0;
	while(ind>0)
	{
		ans+=bit[pos][ind];
		ind=ind-(ind&-ind);
	}
	return ans;
}

int main()
{
	cin>>n>>q;
	string s;
	cin>>s;
	for(ll i=0;i<n;i++)
		update(i+1,1,s[i]-'a');
	ll L,R,choice;
	char x;
	while(q--)
	{
		cin>>choice;
		if(choice==1)
		{
			cin>>L>>x;
			update(L,1,x-'a');
			update(L,-1,s[L-1]-'a');
			s[L-1]=x;
		}
		else
		{
			cin>>L>>R;
			ll cur,odd;
			odd=0;
			for(ll i=0;i<26;i++)
			{
				cur=query(R,i)-query(L-1,i);
				//cout<<cur;
				if(cur%2)
					++odd;
			}
			//cout<<odd<<" ";
			if(odd<=1)
				cout<<"yes\n";
			else
				cout<<"no\n";
		}
	}
	return 0;
}