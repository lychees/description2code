#include <iostream>
using namespace std;

int main()
{
    int i,j,num,s;
    int* studs = NULL;
    string str;
    cin >> num;
    cin >> str;

    studs = new int[num];
    for(i=0;i<num;i++)
        studs[i]=1;
    s=num;
    j=0;
    for(i=0;i<str.size();i++){
    	if (studs[j] != 1){
            while (studs[j] != 1 && j<num){
                j++;
                if (j==num) j=0;
            }
        }
        if (str[i]=='b'){
            studs[j]=0;
            --s;
        }
        if (i==str.size()-1)
            i=-1;
        if(j<num-1) j++;
        else j=0;
        if (s==1)
            break;
    }
    for(i=0;i<num;i++){
        if (studs[i]==1){
            cout << i+1;
        }
    }
    return 0;
}
