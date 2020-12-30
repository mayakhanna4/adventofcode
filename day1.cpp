// Your First C++ Program

#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>


using namespace std;

int twoSum(vector<int> list, int target){
  cout << "TWO SUM CALLED" << endl;
  unordered_map<int, int> hash;
  for(int x=0; x<list.size(); ++x){
    int to_find = target - list[x];
    if(hash.find(to_find) != hash.end()){
      cout << "FOUND" << endl;
      // cout << hash.find(list[x])->first << endl;
      cout << "target:"<< target << endl;
      cout << to_find << endl;
      cout << list[x] << endl;
      return 1;
    }
    hash[list[x]]=x;
  }
  return 0;
}


int main() {
    // ifstream myfile;
    //vector<int> storage;
    // myfile.open("input.txt");
    // int i;
    // while(myfile){
    //   myfile >> i;
    //   storage.push_back(i);
    // }
    // cout << storage.size() << endl;
    // for(int i=0; i<storage.size(); ++i){
    //   int to_look = 2020-storage[i];
    //   for(int x=i+1; x<storage.size(); ++x){
    //     if(storage[x] == to_look){
    //       cout << "FOUND" << endl;
    //       cout << storage[i] << endl;
    //       cout << storage[x] << endl;
    //       return 0;
    //     }
    //   }
    // }
    //
    // myfile.close();


    cout << "What is the target number "<<endl;
    int target_num;
    cin >> target_num;
    vector<int> storage;

    // Hash table solution for Two Sum
    ifstream myfile;
    int i;
    myfile.open("input.txt");
    while(myfile){
      myfile >> i;
      storage.push_back(i);
    }
    for(int x=0; x<storage.size();++x){
        int new_target=target_num - storage[x];
        if(twoSum(storage,new_target) == 1){
          cout << endl;
          cout << "intial val " << storage[x] <<endl;
          cout << " 2nd target val" << new_target <<endl;
          return 0;
        }
        else{

        }

    }


    return 0;

}
