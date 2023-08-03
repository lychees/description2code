#include <cstdio>
#include <vector>
#include <cstdlib>
#include <algorithm>
using namespace std;
vector<pair<long long, long long> > vec;
int main(){
	int N;
	long long S, E, x, d;
	long long left, right, ans;
	scanf("%d %lld %lld", &N, &S, &E);
	for(int i=0; i<N;i++){
		scanf("%lld %lld", &x, &d);
		left = x-d;
		right = x+d;
		if ((right<=S) or (left>=E))
			continue;
		left = max(left, S);
		right = min(right, E);
		vec.push_back(make_pair(left, right));
	}
	if(vec.size()==0){
		printf("%lld\n", E-S);
		return 0;
	}
	sort(vec.begin(), vec.end());
	left = vec[0].first;
	right = vec[0].second;
	ans = max(0LL, left-S);
	/*for(int i=1;i<N;i++){
		if(vec[i].second>right){
			right = vec[i].second;
			//incorrect for now, only add if you know you have seen S
			ans = ans + max(0, vec[i].first - right);
		}
	}*/
	for(int i=1;i<vec.size();i++){
		if(vec[i].second>right){
			//printf("%lld\n", ans);
			ans = ans + max(0LL, vec[i].first - right);
			right = vec[i].second;
		}
	}
	ans = ans + max(0LL, E - right);
	printf("%lld\n", ans);
	return 0;
}