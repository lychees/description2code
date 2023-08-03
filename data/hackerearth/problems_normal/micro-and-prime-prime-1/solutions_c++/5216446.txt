#include<iostream>
#include<cmath>
using namespace std;

const int maxn = 1000001;
long long int arr[maxn] = {0};
long long int arrprime[79502] = {0};
long long int pp[1000001]={0};

void sievealgo(){
    long long int i,j=0;
    arr[0]=1;arr[1]=1;
    for (i=2;i<(long long int)sqrt(maxn);i++)
        if (arr[i]==0)
            for (j=i;i*j<maxn;j++)
                arr[i*j]=1;
    j=0;
    for (i=2;i<maxn;i++){
        if(arr[i]==0)
            arrprime[j++]=i;
    }

    long long int k,p=0,q=0;
	pp[0]=0;
	pp[1]=0;
	for(k=2;k<maxn;k++){
		if(arr[k]==0){
			p++;
		}
		if(arr[p]==0)
			pp[k]=++q;
		else
			pp[k]=q;
	}
}

int main(){
    long long int i,rev,j,s,e,sp,ep,tc,cnt;
    long long int setp[maxn] = {0};
    sievealgo();

    cin >> tc;

    while(tc-- > 0){
        cin>>s>>e;
		cnt=pp[e]-pp[s-1];
		cout<<cnt<<endl;
    }

    return 0;
}
