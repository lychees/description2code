#include <stdio.h>
#include<string.h>
 
int main()
{
int t,i,j;
char a[1000];
char b[1000];
int len1,len2,m,n,ans,result;
int cycle[10]={0,1,6,1,6,5,6,1,6,1};
 
 
scanf("%d",&t);
 
for(i=0;i<t;i++)
{
result=1;
scanf("%s",a);
len1=strlen(a);
scanf("%s",b);
len2=strlen(b);
 
 
m=a[len1-1]-'0';
 
if(len2>1)
n=10*(b[len2-2]-'0')+(b[len2-1]-'0');
else
n=b[len2-1]-'0';
 
 
 
ans=n%4;
if(ans==0)
{
	printf("%d\n",cycle[m]);
}
else
{
	for(j=0;j<ans;j++)
	{
		result=result*m;
	}
	if(result<10)
	printf("%d\n",result);
	else
	printf("%d\n",result%10);
}
 
}
 
return 0;
 
}
