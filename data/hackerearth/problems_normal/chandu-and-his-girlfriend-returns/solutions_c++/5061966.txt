#include <iostream>
using namespace std;

int main()
{
    long int tc,count1,count2,i,j,k,total;
    cin >> tc;
    int* a1 = NULL; int* a2 = NULL;int* a3 = NULL;
    while(tc-- >0)
    {
        cin >> count1 >> count2;
        a1 = new int[count1];
        a2 = new int[count2];
        for (i=0;i<count1;i++){
            cin >> a1[i];
        }
        for (i=0;i<count2;i++){
            cin >> a2[i];
        }

        i=0;j=0;k=0;
        total = count1+count2;
        a3 = new int[total];

        while (j<count1 && k<count2){
            if (a1[j]>a2[k]){
                a3[i++]=a1[j++];
            }
            else{
                a3[i++]=a2[k++];
            }
        }
        while (j<count1){
            a3[i++]=a1[j++];
        }
        while (k<count2){
            a3[i++]=a2[k++];
        }
        for (i=0;i<total;i++){
            cout << a3[i] << " ";
        }
        cout << endl;
    }
    return 0;
}
