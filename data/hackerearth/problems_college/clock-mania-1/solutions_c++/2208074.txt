#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--)
	{
	    int h,m,m1,d;
	    cin>>h>>m;
	    m1=m;
	    m=m*6;
	    h=h*30+m1/2;
	    d=abs(h-m);
	    if(d>180)
	        d=360-d;
	    cout<<d<<endl;
	}
	return 0;
}
