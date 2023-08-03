#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int arrays[100009];
bool compare(int a,int b){
	return a > b;
}
int main(){
	int T;
	scanf("%d",&T);
	int N,K;
	while(T--){
		scanf("%d %d",&N,&K);
		for(int i=0;i<N;i++){
			scanf("%d",&arrays[i]);
		}
		long int ans = 0;
		if(K>=N){
			for(int i=0;i<N;i++)
				ans+= arrays[i];
		}else{
			sort(arrays,arrays+N,compare);
			for(int i=0;i<K;i++){
				ans+=arrays[i];
			}
		}
		printf("%ld\n",ans);
	}
	return 0;
}