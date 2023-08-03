#include<iostream>
#include<cmath>
using namespace std;

const int maxn = 1000001;
unsigned long long int arr[maxn] = {0};
unsigned long long int ans[maxn] = {0};

void sievealgo(){
    unsigned long long int i,j=0;
    for (i=2;i<(long long int)sqrt(maxn);i++)
        if (arr[i]==0)
            for (j=i;i*j<maxn;j++)
                arr[i*j]=1;
    for(i=2;i<maxn;i++)
		if(!arr[i]) ans[i]=ans[i-1]+i;
		else ans[i]=ans[i-1];
}

int main(){
    unsigned long long int sum,i,n,cnt,tc,s,e,sp,ep;

    sievealgo();

    cin >> tc;

    while(tc-- > 0){
        sp=0;ep=0;
        cin >> s >> e;
        cout << ans[e]-ans[s-1] << endl;
    }
    return 0;
}
