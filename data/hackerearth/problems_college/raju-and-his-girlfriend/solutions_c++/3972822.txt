#include <iostream>
#include<string.h>

using namespace std;


int keyloc(char a)
{
	if(a=='a'||a=='b'||a=='c'||a=='2')
	return 2;
	
	else if(a=='.'||a==','||a=='?'||a=='!' || a=='1')
	return 1;
	
	else if(a=='d'||a=='e'||a=='f'|| a=='3')
	return 3;
	
	else if(a=='g'||a=='h'||a=='i'|| a=='4')
	return 4;
	
	else if(a=='j'||a=='k'||a=='l'|| a=='5')
	return 5;
	
	else if(a=='m'||a=='n'||a=='o'|| a=='6')
	return 6;
	
	else if(a=='p'||a=='q'||a=='r'|| a=='7' || a=='s')
	return 7;
	
	else if(a=='t'||a=='u'||a=='v'|| a=='8' )
	return 8;
	
	else if(a=='w'||a=='x'||a=='y'|| a=='9' || a=='z')
	return 9;
	
	else if(a=='_' ||  a=='0')
	return 0;

	
}


int nsec(char a)
{
	
	if(a=='a' || a=='.' || a=='d' || a=='g' || a=='j' || a=='m' || a=='p' || a=='t' || a=='w' || a=='_' )
	return 1;
	
	else if(a=='b' || a==',' || a=='e' || a=='h' || a=='k' || a=='n' || a=='q' || a=='u' || a=='x' || a=='0' )
	return 2;
	
	else if(a=='c' || a=='?' || a=='f' || a=='i' || a=='l' || a=='o' || a=='r' || a=='v' || a=='y' )
	return 3;
	
	else if(a=='2' || a=='!' || a=='3' || a=='4' || a=='5' || a=='6' || a=='s' || a=='8' || a=='z' )
	return 4;
	
	else if(a=='1' || a=='7' || a=='9' )
	return 5;
	
	
	
	
	
	
}


int main()
{
	int t,i,j,k,prev,pres,count,x,y,z,end;
	char s[100000];
	
    cin>>t;
    while(t--)
    {
    	cin>>x;
    	cin>>y;
    	cin>>z;
    	count=0;
    	cin>>s;
    	prev=1;
    	pres=1;
    	end=0;
    	for(i=0;i<strlen(s);i++)
    	{
    		pres=keyloc(s[i]);
    		if(prev!=pres)
    		count+=x;
    		
    		prev=pres;
    		count=count+nsec(s[i])*y;
    		if(count<=z)
    		end++;
    		
    	}
    	
  for(i=0;i<end;i++)
  cout<<s[i];
  
  cout<<endl;
  
    	
    	
    }
    return 0;
}
