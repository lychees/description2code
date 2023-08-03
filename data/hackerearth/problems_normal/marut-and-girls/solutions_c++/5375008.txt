#include<bits/stdc++.h>
using namespace std;
int main()
{
    //ios::sync_with_stdio(false);
    int M,i,N;
    int good[10001]={0},num;
    cin>>M;
    assert(1<=M && M<=100);
    int repeat=0;
    for(i=0;i<M;i++)
    {
        cin>>num;
        assert(1<=num && num<=10000);
        assert(good[num]==0);
        if(good[num]==0)
        	good[num]=1;
       
    }
   
    cin>>N;
    assert(1<=N && N<=9000);
    char s[2]; 
    gets(s);
  
    int ans=0;
    while(N--)
    {
    	int done[100001]={0};
        char ch;
        int num=0;
        int thisone=0;
        char str[1000001];
      
        gets(str);
    
        int i=0;
        int count=0;
        while(str[i]!='\0')
        {
        	ch=str[i];
            if(ch==' ')
            {
            	count++;
            	assert(done[num]==0);
       			assert(1<=num && num<=10000);
        		done[num]=1;
                if(good[num]==1)
                {
                	thisone++;
                }
        		
                num=0;
            }
            else
            {
                num=num*10+(ch-'0');
                
            }
            i++;
            
        }
        if(num!=0)
        {
        	count++;
        	assert(done[num]==0);
        	
        	if(good[num]==1)
                    thisone++;
        }
        assert(1<=count && count<=1000);
      
        if(thisone==M)
        {
            ans++;
        }
    
      
    }
     cout<<ans<<endl;
    return 0;
}  