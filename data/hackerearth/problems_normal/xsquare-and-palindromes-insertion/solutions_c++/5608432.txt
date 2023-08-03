#include <iostream>

using namespace std;

int main (){
    int tc,i;
    string str;

    cin >> tc;
    while(tc-- > 0){
        int arr[26]={0};
        int odd=0;
        cin >> str;
        for(i=0;i<str.size();i++) arr[str[i]-97]++;
        for(i=0;i<26;i++){
            if(arr[i]%2!=0)
                odd++;
        }
        if(odd==0) cout << 0;
        else cout << odd-1;
        cout << endl;
    }
    return 0;
}
