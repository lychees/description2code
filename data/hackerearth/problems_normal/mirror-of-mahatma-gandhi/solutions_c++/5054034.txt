#include <iostream>
using namespace std;

int main()
{
    int tc,len,i,mi,temp;
    string num;
    cin >> tc;
    while(tc-- >0)
    {
        cin >> num;
        mi = 1;
        len = num.size();
        for (i=0;i<len;i++){
            if ((num[i]=='0') || (num[i]=='1') || (num[i]=='8')){
                continue;
            }
            else{
                cout << "NO";
                mi = 0;
                break;
            }
        }
        if (mi == 1){
            temp = len;
            for (i=0;i<len/2;i++){
                if (num[i]!=num[temp-1]){
                    cout << "NO";
                    mi = 0;
                    break;
                }
                temp--;
            }
        }
        if (mi == 1){
            cout << "YES";
        }
        cout << endl;
    }
    return 0;
}
