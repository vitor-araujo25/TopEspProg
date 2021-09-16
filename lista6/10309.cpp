#include <iostream>
#include <stdio.h>
#include <cmath>

using namespace std;

bool original[10][10];
bool copy_[10][10];

bool isGoal() {

	for (int i = 0; i < 10; i++) {
		if (copy_[9][i]) {
			return false;
		}
	}

	return true;
}

void press(int i, int j) {
	copy_[i][j] = !copy_[i][j];
	
	if(i-1 >= 0) 
		copy_[i-1][j] = !copy_[i-1][j];
	if(j-1 >= 0)
		copy_[i][j-1] = !copy_[i][j-1];
	if(i+1 < 10)
		copy_[i+1][j] = !copy_[i+1][j];
	if(j+1 < 10)
		copy_[i][j+1] = !copy_[i][j+1];

}

int main() {

	int current = 0;
	int minimal = 101;

	string name;
	char temp;

	while (true) {

		cin >> name;
		if (name.compare("end") == 0) break;

		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				cin >> temp;
				original[i][j] = (temp == 'O');
			}
		}
		minimal = 101;

		for (int k = 0; k <= 1023; k++) {
	
			current = 0;

			for (int i = 0; i < 10; i++) {
				for (int j = 0; j < 10; j++) {
					copy_[i][j] = original[i][j];
				}
			}

			int l = k;
			for (int i = 0; i < 10; i++) {

				if (l & 1) {
					press(0, i);
					current++;
				}
				l >>= 1;

			}

			for (int i = 0; i < 9; i++) {
				for (int j = 0; j < 10; j++) {
					if (copy_[i][j]) {
						press(i + 1, j);
						current++;
					}
				}
			}
			if (isGoal()) {
				minimal = min(minimal, current);
			}
		}

		printf("%s %d\n", name.c_str(), minimal);
	}

	return 0;
}