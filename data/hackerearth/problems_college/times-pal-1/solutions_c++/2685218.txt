#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
using namespace std;

int main()
{
	int t,len;
	string a,b,temp;
	cin>>t;
	while(t--)
	{
		int cnt=0;
		cin>>a>>b;
		len = a.size();
		temp = a;
		for(int i=0;i<=len;i++)
		{
			temp.insert(i,b);
			//cout<<"\n at i = "<<i<<" , string = "<<temp<<endl;
			if(temp == string(temp.rbegin() , temp.rend()) )cnt++;
			temp = a;
		}
		cout<<cnt<<endl;
	}
}
