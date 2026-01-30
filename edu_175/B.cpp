#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){
    int ntc;
    cin >> ntc;
    while(ntc--){
        int n,x;
        long long int k;
        string order;
        int p1=0;
        cin >> n >> x >> k;
        cin >> order;
        long long int zcount=0;
        long long int timer=k;
        while(timer-- && p1<order.length()){
            if(order[p1]=='L'){x -= 1;}
            else{x += 1;}
            p1 += 1;
            
            if(x==0){
                if(zcount == 0){zcount += 1;}
                else{
                    // cout << timer << "s and " << p1 << endl;
                    zcount += (timer-1)/(p1) + 1;
                    // cout << zcount << ' ';
                    break;
                }
                p1 = 0;
            }
        }
        cout << zcount << endl;
    }
    return 0;
}