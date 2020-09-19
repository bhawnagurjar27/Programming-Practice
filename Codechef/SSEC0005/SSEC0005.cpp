#include <bits/stdc++.h>
using namespace std;
int main()
{
int number_of_test_cases;
cin >> number_of_test_cases;

while(number_of_test_cases--)
{
  string wrong_password;
  cin >> wrong_password;
  
  int len_of_wrong_password = wrong_password.length();
  
  for(int i = 0; i < len_of_wrong_password; i++)
  {
    wrong_password[i] = wrong_password[i] - 2;
  }
 
  
  cout << wrong_password << endl;     // Original Password

}
   return 0;
}
