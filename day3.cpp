#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>


using namespace std;

int sled(vector<string> storage, int x, int y){
  int tree_count = 0;
  int r = 0;
  int c = 0;
  while(r < storage.size() - 1){
    if(storage[r][c] == '#'){
      tree_count++;
    }
    r = r + y;
    c = c + x;
    if(c >= storage[0].length()){
      c = c - storage[0].length();
    }
  }
  return tree_count;
}

int main(){
  ifstream myfile;
  myfile.open("day3.txt");
  vector<string> storage;
  while(myfile){
    string str;
    getline(myfile, str);
    storage.push_back(str);
  }

  int a = sled(storage, 1, 1);
  int b = sled(storage, 3, 1);
  int c = sled(storage, 5, 1);
  int d = sled(storage, 7, 1);
  int e = sled(storage, 1, 2);

  cout << a << endl;
  cout << b << endl;
  cout << c << endl;
  cout << d << endl;
  cout << e << endl;
  long ex = (long)(a*b*c*d)*(long)44;
  cout << ex << endl;
  long f = 9354744432;
  cout << f << endl;


  cout << a*b*c*d*e << endl;



  return 0;
}
