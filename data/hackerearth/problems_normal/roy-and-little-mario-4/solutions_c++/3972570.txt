#include <iostream>
#include<stdio.h>
using namespace std;
#define MOD 1000000007
#define LL long long int
int main() {
    int t,N,i;
	LL tribonacci[100010];
	tribonacci[0]=0,tribonacci[1]=0,tribonacci[2]=1;
	for(i=3;i<100010;i++) tribonacci[i]=(tribonacci[i-1]+tribonacci[i-2]+tribonacci[i-3])%MOD;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&N);
		printf("%lld\n",tribonacci[N+2]);
	}
	return 0;
}
