#include<iostream>
#include<stack>
using namespace std;
int main()
{
    stack<int> s;
    int sz,i,q,cost;
    cin >> sz;
    for(i=0;i<sz;i++){
        cin >> q;
        if(q==1){
            if(s.empty()) cout << "No Food";
            else { cout << s.top();s.pop(); }
            cout << endl;
        }
        if(q==2){
            cin >> cost;
            s.push(cost);
        }
    }
    return 0;
}
