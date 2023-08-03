#include<iostream>
#include<algorithm>
using namespace std;


bool cmp(int a, int b)
{
    return a<b;
}

int main()
{
    int t;
    cin>>t;

    while(t--)
    {
        int n;
        cin>>n;
        int men[n];
        int women[n];

        for(int i=0;i<n;i++)
            cin>>men[i];
        for(int i=0;i<n;i++)
            cin>>women[i];

        sort(men,men+n);
        sort(women,women+n,cmp);

        int sum=0;

        for(int i=0;i<n;i++)
        {
            sum+=men[i]*women[i];
        }

        cout<<sum<<endl;
    }
}
