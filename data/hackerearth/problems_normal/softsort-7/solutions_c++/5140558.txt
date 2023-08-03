#include<iostream>

using namespace std;

int main(){
    long long int tc,i,num,mod=1000000007,res,m=1000001;
    long long f[m];

    f[0] = f[1] = 1;

    for(i=2;i<=m;i++){
    	f[i] = (f[i-1]*i)% mod;
    }

    cin >> tc;

    while (tc-- > 0){
        cin >> num;
        cout << (f[num]+2*(f[num]-1)+5)%mod << endl;
    }

    return 0;
}
