#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    string x,y;
    int i=0;
    cin>>x;
    int n=x.length();
    for(i=0;i<n/2;i++)
    {
        y[i]=x[n-i-1];
        y[n-i-1]=x[i];
    }
    if(n%2==1)
    {
        y[(n-1)/2]=x[(n-1)/2];
    }
    for(i=0;i<n-1;i++)
    {
        cout<<x[i]<<"-";
    }
    cout<<x[i]<<endl;
    for(i=0;i<n-1;i++)
    {
        cout<<y[i]<<"-";
    }
    cout<<y[i]<<endl;
    return 0;
}
