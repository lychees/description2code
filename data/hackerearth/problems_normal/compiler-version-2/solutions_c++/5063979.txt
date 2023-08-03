#include <bits/stdc++.h>

using namespace std;
//	  https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/compiler-version-2/description/
int main()
{
    string s, c;
   
    while(getline(cin , s)){

        bool con = false;
        c = "";

        for(int i = 0; i < s.size(); i++){

            if(con){

                c += s[i];
                continue;
            }

            if(i < s.size() - 1 && s[i] == '/' && s[i + 1] == '/')  {

                c += "//";
                con = true;
                i++;
            }

            else if(i < s.size() - 1 && s[i] == '-' && s[i + 1] == '>'){

                c += '.';
                i++;

            } else
				c += s[i];
        }

        cout << c << "\n";
    }

    return 0;
}







