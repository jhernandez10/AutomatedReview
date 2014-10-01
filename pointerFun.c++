#include <stdio.h>
#include <iostream>

using namespace std;


int main (){
	std::string answer;
	cout << "\nint i = 2\nint* p = &i\nint& r = p\nDoes this compile?:";
	cin >> answer;
	cout << answer <<endl;
	cout << "This is coming from the c++ program" << endl;
	return 0;
}