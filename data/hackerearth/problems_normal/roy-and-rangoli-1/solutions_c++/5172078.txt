#include<iostream>
#include<cmath>
using namespace std;

int main(){
    long long int i,n,j,result=0,cnt=0,g,b;
    cin >> n;

    for(i=2;i<=2*(n-1);i++){
        b=1;
		for(j=2;j<=(long long int)sqrt(i);j++){
				if(i%j==0){
					b=false;
					break;
				}
			}
        if(b&&i<n){
            cnt=i+1;
            result=(result+cnt)%1000000007;
        }
        if(b&&i>n-1){
            cnt=2*n-i-1;
            result=(result+cnt)%1000000007;
        }
    }

    cout << result%1000000007 << endl;;

	return 0;
}
