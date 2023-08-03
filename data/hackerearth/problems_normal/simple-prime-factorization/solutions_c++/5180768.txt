#include<iostream>
#include<cmath>
using namespace std;

const int maxn = 1000001;
int arr[maxn] = {0};
int arrprime[79502] = {0};

void sievealgo(){
    long long int i,j=0;
    for (i=2;i<(long long int)sqrt(maxn);i++)
        if (arr[i]==0)
            for (j=i;i*j<maxn;j++)
                arr[i*j]=1;
    j=0;
    for (i=2;i<maxn;i++){
        if(arr[i]==0)
            arrprime[j++]=i;
    }
}

int main(){
    int i,n,cnt,tc,done;
    int arrnum[79502][1]={0};

    sievealgo();

    cin >> tc;

    while(tc-- > 0){
        done=0;
        cin >> n;
        cnt=0;
        for(i=0;i<79502;i++){
            if(arrprime[i]==n){
                done = 1;
                cout << "2^0";
                break;
            }
        }
        if(!done){
            for(i=0;i<79502;i++){
                cnt=0;
                while(n%arrprime[i]==0){
                    cnt++;
                    n=n/arrprime[i];
                }
                if (arrprime[i]==2) cout <<"2^"<<cnt;
                else if (cnt>0) cout <<"*"<<arrprime[i]<<"^"<<cnt;

                if(n==1) break;
            }
        }
        cout << endl;
    }
    return 0;
}
