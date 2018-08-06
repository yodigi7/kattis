#include <iostream>
#include <string>
using namespace std;

int main() {
  string word;
  cin >> word;
  int answer = word.length();
  for (int i = 0; i < word.length(); i++) {
    if(i == 0 && word[i] == 'P') {
      answer -= 1;
    }
    else if (i % 3 == 0 && word[i] == 'P') {
      answer -= 1;
    }
    else if (i % 3 == 1 && word[i] == 'E') {
      answer -= 1;
    }
    else if (i % 3 == 2 && word[i] == 'R') {
      answer -= 1;
    }
  }
  cout << answer;
  return 0;
}
