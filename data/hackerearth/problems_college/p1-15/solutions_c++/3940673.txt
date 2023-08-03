#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
   	cin>>t;
   	while(t--)
   	{
   		string str1;
   		string str2;
   		int pos;
   		int flag=0;
   		cin>>str1>>str2;
   		cout<<str1;
   		int l1=str1.length();
   		int l2=str2.length();
   		int i=0,j=0,k=0;
   		
   			while(str1[i]!='\0')
   			{
   				if(str1[i]==str2[0])
   				{
   					if(str1.substr(i)==str2.substr(0,l1-i))
   					{
   						pos=l1-i;
   						flag=1;
   						break;
   					}
   				}
   				i++;
   			}
   			if(flag==1)
   			{
   				for(i=pos;str2[i]!='\0';i++)
   				{
   					cout<<str2[i];
   				}
   				cout<<endl;
   			}
   			else
   			{
   				cout<<str2<<endl;
   			}
   	}
}
