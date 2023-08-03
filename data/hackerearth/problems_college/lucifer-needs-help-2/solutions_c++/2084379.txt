#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

ll arr[1000010];
ll tmp[1000010];

#define s(x) scanf("%lld", &x)

int main()
{
    ll n, i, j, k, m;
    s(n);
    for (i = 1; i <= n; i++)
        s(arr[i]);
    s(m);
    while (m--) {
        s(i);
        s(j);
        s(k);
        tmp[i] += k;
        tmp[j+1] -= k;
    }
    for (i = 1; i <= n; i++)
        tmp[i] += tmp[i-1];
    for (i = 1; i <= n; i++)
        printf("%lld\n", arr[i]+tmp[i]);
    return 0;
}