#include<bits/stdc++.h>
using namespace std;
int main()
{
	map<string, int> M;
	map<string, int> :: iterator it;
	int N;
	cin>>N;
	for(int i=0;i<N;i++)
	{
		string s;
		cin>>s;
		sort(s.begin(),s.end());
		M[s]+=1;
	}
	int max=-1;
	for(it=M.begin();it!=M.end();it++)
	{
		if(it->second>max)
			max=it->second;
	}
	cout<<max<<endl;
	return 0;
}