#include<stdio.h>
int main(void){
long long int t,res,n,k;
scanf("%d",&t);
while(t--){
scanf("%lld%lld",&n,&k);
res=n*(n+1)/2;
if(res>=k)
printf("YES\n");
else
printf("NO\n");}
return 0;
}
