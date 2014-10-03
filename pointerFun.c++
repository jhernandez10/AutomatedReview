#include <stdio.h>
#include <iostream>

using namespace std;

int compiles1(){
	std::string answer;
	cout << "\nint i = 2\nint* p = &i\nint& r = p\nDoes this compile?(yes or no):";
	cin >> answer;
	cout << answer <<endl;
	if(answer[0] == 'y'){
		cout << "Correct!!" << endl;
		return 1;
	}
	cout << "Incorrect, This is a perfectly valid way to assign a reference and pointer" << endl;
	return 0;
}

int compiles2(){
	std::string answer;
	cout << "\nint i = 2\nint* p = &i\nint& r = p\n";
	cout << "\n++*r\nassert(&r == &i)\nDoes this assertion fail?(yes or no):" <<endl;
	cin >> answer;
	if(answer[0] == 'n'){
		cout << "Correct!!" << endl;
		return 1;
	}
	cout << "Incorrect, once a reference is tied to something it is indistinguishable from the original\n" << endl;
	return 0;
}


int main (){
	int total = 2;
	int score = 0;

	score = score + compiles1();
	score = score + compiles2();

	float percentage = (float)(score/total) * 100;
	cout << percentage << endl;
	return 0;
}