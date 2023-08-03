#include<iostream>
using namespace std;
#define max1 1000
int dist(int,int,int,int);
int main()
{
	int N,NN;
	cin>>N;
	NN=N;
	int x[max1],y[max1],r[max1];
	int i=0;
	for(i=0;i<N;i++)
	{
		cin>>x[i]>>y[i]>>r[i];
	}
	int k,j,l,count=0,final=0;
	for( k=1;k<=1000;k++)
	{
		for(j=1;j<=1000;j++)
		{
			for(l=0;l<NN;l++)
			{
				if(dist(k,j,x[l],y[l])<=r[l]*r[l])
				{
					count++;
				}
			}
			if(count>=2 && NN>=2)
			{
				final++;
			}
			count=0;
		}
	}
	cout<<final;
	return 0;
}

int dist(int a,int b,int p,int q)
{
	int val;
	val=(a-p)*(a-p)+(b-q)*(b-q);
	return val;
}
