#include <iostream>

using namespace std;

int main() {
    int icount,sum=0,i,max_ending_here=0,max_so_far;
    int* arr=NULL;
    cin >> icount;
    arr = new int[icount];
    for (i=0;i<icount;i++){
        cin >> arr[i];
    }
    for (i = 0; i < icount; i++)
    {
        max_ending_here = max_ending_here + arr[i];
        if (max_ending_here < 0)
            max_ending_here = 0;
        if (max_so_far < max_ending_here)
            max_so_far = max_ending_here;
    }
    cout << max_so_far;
    return 0;
}
