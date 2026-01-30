#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){
    int ntc;
    cin >> ntc;
    while(ntc--){
        int n;
        cin >> n;
        int count=0;
        if(n<15){count=min(n%15,2)+1;}
        else{
            count = (n/15)*3 + min(n%15, 2) + 1;
        }
        cout << count << endl;
    }
    return 0;
}