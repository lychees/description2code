    #include <iostream>
    using namespace std;
     
    #define mod 1000000009
     
    long long power(long long x, long long y){
        long long ans = 1;
        while(y){
            if(y&1){
                ans = (ans*x)%mod;
            }
            x = (x*x)%mod;
            y >>= 1;
        }
        return ans;
    }
     
    int main()
    {
        long long t,n;
        cin >> t;
        while(t--){
            cin >> n;
            cout << (((power(10,n) - power(8,n) + mod)%mod)*power(2,mod-2))%mod << endl;
        }
        return 0;
    }