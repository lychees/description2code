#include <iostream>
#include <algorithm>

#define MAX 1000000

using namespace std;

int max(long a, long b)
{
	return (a >= b ? a : b);
}

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
    long t,n,i,k,id,a[MAX],d[MAX],cnt,Max;
    cin >> t;
    while (t--)
    {
    	Max = - 1;
    	cin >> n >> k;
    	for (i = 0; i < n; i++)
    	  cin >> a[i];
    	cin >> d[0];
    	for (i = 1; i < k; i++)
    	{
    	   cin >> cnt;
    	   d[i] = max(d[i-1],cnt);
    	}
    	for (i = 0; i < n; i++)
    	{
    		cnt = upper_bound(d,d+k,a[i]) - d;
    		if (cnt > Max)
    		{
    			Max = cnt;
    			id = i;
    		}
    	}
    	cout << id << "\n";
    }
    return 0;
}
