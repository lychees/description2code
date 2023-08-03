#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main()
{
    string x;
    cin>>x;
    for(int i=0;i<x.length();i++)
        cout<<"-"<<int(x[i])+1<<" ";
    cout<<endl;
    return 0;
}
