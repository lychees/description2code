//https://www.hackerearth.com/code-monk-greedy-technique/algorithm/arjit-and-apex/
#include <iostream>
#include <vector>
#include <set>
using namespace std;
int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	while(t--){
		std::vector<set<int> > vec1(10001);
		std::vector<set<int> > vec2(10001);
		set<int>::iterator it,it2;
		int g=0,h=0;
		int ge,he,m,n,u,v;
		cin>>m>>n;
		for(int i=0;i<m;i++){
			cin>>u>>v;
			vec1[u].insert(v);
		}
		//now the bad part.forgive me Torvalds :(
		for(int i=0;i<n;i++){
			cin>>u>>v;
			vec2[u].insert(v);
		}
		//cout<<"*****************"<<g<<"  "<<h<<endl;
		cin>>ge>>he;
		for(int i=0;i<10001;i++){
			it=vec2[i].begin();
			g+=((vec2[i].size()>vec1[i].size())?(vec1[i].size()):(vec2[i].size()));
			while(!vec1.empty() && it!=vec2[i].end()){
				it2=vec1[i].find(*it);
				if(it2!=vec1[i].end()){
					h++;
					vec1[i].erase(it2);
				}
				it++;
			}
		}
		if(ge<=g&&he<=h) cout<<"Great\n";
		else if(ge<=g) cout<<"Good\n";
		else cout<<":(\n";
	}
	return 0;
}