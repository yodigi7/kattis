#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>

int main(){
  vector<double> prices;
  double p,a,b,c,d,n;
  
  //Get input
  cin >> p >> a >> b >> c >> d >> n;
  for(int k = 0; k < n; k++){
    prices.push_back(p*sin(a*k+b)+cos(c*k+d)+2);
  }
  
  //Find largest decrease
  
  
  return 0;
}
