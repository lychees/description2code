#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main()
{
    int n,i,j,q;
    cin>>n>>q;
    int a[n][n];
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            cin>>a[i][j];
        }
    }
    while(q--)
    {
        long int b;
        cin>>b;
        if(b%360==0)
        {
            for(i=0;i<n;i++)
            {
                for(j=0;j<n;j++)
                {
                    cout<<a[i][j]<<" ";
                }
                cout<<endl;
            }
        }
        else if(b%360==90)
        {
            for(j=0;j<n;j++)
            {
                for(i=n-1;i>=0;i--)
                {
                    cout<<a[i][j]<<" ";
                }
                cout<<endl;
            }
        }
        else if(b%360==180)
        {
            for(i=n-1;i>=0;i--)
            {
                for(j=n-1;j>=0;j--)
                {
                    cout<<a[i][j]<<" ";
                }
                cout<<endl;
            }
        }
        else
        {
            for(j=n-1;j>=0;j--)
            {
                for(i=0;i<n;i++)
                {
                    cout<<a[i][j]<<" ";
                }
                cout<<endl;
            }
        }
        cout<<endl;
    }
    return 0;
}
