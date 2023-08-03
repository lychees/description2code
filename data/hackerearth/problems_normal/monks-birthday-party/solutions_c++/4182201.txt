#include <bits/stdc++.h>
using namespace std;
typedef long long int lli;
int main(){
    int t;cin>>t;
    while(t--){
        int n;cin>>n;string str;
        set<string>s;set<string>::iterator it;
        while(n--){cin>>str;s.insert(str);}
        for(it=s.begin();it!=s.end();++it) cout<<*it<<endl;
    }
}