#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    unsigned long int t,n;
    unsigned long int count[1000001];
    unsigned long int maxVal;
    int maxIndex;
   
    
    cin>>t;
    while(t--)
    {
        for(int i=0;i<=1000000;i++)
            count[i]=0;
    vector<int> v;     
        cin>>n;
        unsigned long int a;
        for(unsigned long int i=0;i<n;i++)
        {   
            cin>>a;
            count[a]+=1;
        }
        
        maxVal=0;
        for(int i=1;i<=1000000;i++)
        {
            if(maxVal==count[i])
            { v.push_back(i);
                
            }
            else if(maxVal<count[i])
            {
                v.erase(v.begin(),v.begin()+v.size());
                v.push_back(i);
                maxVal=count[i];
            }
            
            
       /*      
        for(int i=0;i<v.size();i++)
            cout<<i<<":"<<v[i]<<" ";
        
        cout<<endl;*/
        }
       
        
        sort(v.begin(),v.end());
        
        for(int i=v.size()-1;i>=0;i--)
            cout<<v[i]<<" ";
    
        cout<<endl;
        
        
    }
    
    return 0;
}
        
            
            