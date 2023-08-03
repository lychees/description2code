#include<iostream>
#include<cmath>
using namespace std;
int sumofdigits(long int num){
	int sum=0;
	long int r;
	while(num){
      r=num%10;
      num=num/10;
      sum=sum+r;
  	}
  	return sum;
}
int main(){
	int T;
	cin>>T;
	long long int N;
	while(T--){
		cin>>N;
		long int a = sqrt(N);
		bool flag = false;
		int count = 0;
		long int i=a;
		for(;i>0;i--){
			count++;
			if(N%i==0){
				if(i*(i+sumofdigits(i))==N){
					//cout<<"Yippy "<<N<<" "<<i<<endl;
					flag = true;
					break;
				}
			}
			if(count>400)
				break;
		}
		if(flag == false){
			cout<<-1<<endl;
		}
		else{
			cout<<i<<endl;
		}
	}
	return 0;
}