#include<iostream>
#include<bits/stdc++.h>
#include<cmath>
#include<vector>
using namespace std;
int main()
{
    long int t,i,j,c;
    cin>>t;
    string x[t];
    for(i=0;i<t;i++)
    {
        cin>>x[i];
    }
    for(i=0;i<t-1;i++)
    {
        for(j=0;j<t-i-1;j++)
        {
            if(x[j]>x[j+1])
                swap(x[j],x[j+1]);
        }
    }
    for(i=0;i<t-1;i++)
    {
        cout<<x[i]<<" ";
        c=0;
        while(x[i]==x[i+1])
        {
            c++;
            i++;
        }
        cout<<c+1<<endl;
    }
    if(x[t-2]!=x[t-1])
        cout<<x[t-1]<<" 1"<<endl;
    return 0;
}
