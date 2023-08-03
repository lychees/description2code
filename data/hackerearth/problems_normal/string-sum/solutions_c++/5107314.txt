#include <iostream>
#include <stdlib.h>
#include <cstring>

using namespace std;

int main() {
    int j,s=0;
    string str;
    cin >> str;

    char myArray[str.size()+1];
    strcpy(myArray, str.c_str());

    int s_len = str.size();

    for(j=0; j<s_len; j++){
        s=s+int(myArray[j])-96;
    }
    cout << s;

    return 0;
}
