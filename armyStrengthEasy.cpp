#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    short numTimes, sGodzilla, sMecha, strength;
    vector<short> godzilla, mecha;
    cin >> numTimes;
    for(int i = 0; i < numTimes; i++){
        cin >> sGodzilla >> sMecha;
        for(int j = 0; j < sGodzilla; j++){
            cin >> strength;
            godzilla.push_back(strength);
        }
        sort(godzilla.begin(), godzilla.end());
        for(int j = 0; j < sMecha; j++){
            cin >> strength;
            mecha.push_back(strength);
        }
        sort(mecha.begin(), mecha.end());
        if(mecha.back() > godzilla.back()){
            cout << "MechaGodzilla" << endl;
        }
        else{
            cout << "Godzilla" << endl;
        }
        godzilla.clear();
        mecha.clear();
    }
    return 0;
}
