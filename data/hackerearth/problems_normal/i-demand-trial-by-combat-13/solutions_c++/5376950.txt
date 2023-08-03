#include <iostream>
using namespace std;

int main()
{
    int tc,sz,cnt,i,j,iszero;
    cin >> tc;
    int* arr = NULL;
    int* arrprev = NULL;
    while(tc-- > 0){
        iszero=1;
        cin >> sz >> cnt;
        arr = new int[sz];
        arrprev = new int[sz];
        for (i=0;i<sz;i++) cin >> arr[i];
        for (i=0;i<cnt;i++){
            iszero=1;
            for (j=0;j<sz;j++){
                if (arr[j]==1){
                    iszero=0;
                    break;
                }
            }
            if (iszero==1) break;
            for (j=0;j<sz;j++) arrprev[j]=arr[j];
            if(arrprev[1]==1) arr[0]=1;
            else arr[0]=0;
            if(arrprev[sz-2]==1) arr[sz-1]=1;
            else arr[sz-1]=0;
            for(j=1;j<sz-1;j++){
                if(arrprev[j-1]==1&&arrprev[j+1]==1) arr[j]=1;
                else arr[j]=0;
            }
        }
        for (i=0;i<sz;i++) cout<<arr[i]<<" ";
        cout << endl;
        delete [] arrprev;
        arrprev = NULL;
        delete [] arr;
        arr = NULL;
    }
    return 0;
}
