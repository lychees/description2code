#include<bits/stdc++.h>
using namespace std;

const int maxn = 70000;
long long int arr[maxn] = {0};
long long int arrprime[79502] = {0};
long long int ans[70000]={0};

long long int dsum(long long int n){
   long long int t,sum=0,remainder;
   t = n;
   while (t != 0){
      remainder = t % 10;
      sum = sum + remainder;
      t = t / 10;
   }
   return sum;
}
void sievealgo(){
    long long int i,j=0,num,cnt,sum,is;
    arr[0]=1;arr[1]=1;
    for (i=2;i<(long long int)sqrt(maxn);i++)
        if (arr[i]==0)
            for (j=i;i*j<maxn;j++)
                arr[i*j]=1;
    j=0;
    for (i=2;i<maxn;i++){
        if(arr[i]==0)
            arrprime[j++]=i;
    }
    for(i=2;i<maxn;i++){
        num = i;
        cnt = 0;
        sum = 0;
        is = dsum(num);
        while (num != 1){
            while (num%arrprime[cnt] == 0){
                num = num/arrprime[cnt];
                sum = sum + dsum(arrprime[cnt]);
                if (num == 1) break;
            }
            cnt++;
        }
        if (sum==is) ans[i]=ans[i-1]+1;
        else ans[i]=ans[i-1];
    }
}
int main(){
    int tc,sum,f,c,s,e,i;
    sievealgo();
    //cout << "Done" << endl;
    scanf("%d",&tc);
    while(tc-- > 0){
        scanf("%d",&s);scanf("%d",&e);
        printf("%d\n",ans[e]-ans[s-1]);
    }
    return 0;
}
