// First, try writing a program that initializes a vector of size 3.
// The values for this vector are [5,10,27].
// Initialize another vector of size 3 with the values [3,17,12].
// Now subtract the two vectors from each other and output the results.
//

#include <iostream>
#include <vector>

using namespace std;

vector<float> vectoraddition(vector<float> vector1, vector<float> vector2);

int main() {

	static const float arr1[] = {5.0, 10.0, 27.0};
	static const float arr2[] = {2.0, 17.0, 12.0};
	vector<float> v1 (arr1, arr1 + sizeof(arr1) / sizeof(arr1[0]));
	vector<float> v2 (arr2, arr2 + sizeof(arr2) / sizeof(arr2[0]));
	vector<float> v3 (v1.size());

	v3 = vectoraddition(v1, v2);

	for (int i = 0; i < v3.size(); i++) {
		cout << v3[i] << " ";
	}

	cout << endl;

	return 0;
}

vector<float> vectoraddition(vector<float> vector1, vector<float> vector2) {

	vector<float> vectorsum (vector1.size());

	for (int i = 0; i < vector1.size(); i++) {
		vectorsum[i] = vector1[i] - vector2[i];
	}

	return vectorsum;
}

  // Initialize a vector with the values [17,10,31,5,7].
  // Initialize another vector with the values [3,1,6,19,8].
  // Then, output another vector that contains the product of each element.
  // In other words, the vector should have [17×3, 10×1, 31×6, 5×19, 7×8].
  //

#include <iostream>
#include <vector>

using namespace std;

vector<float> vectormultiply(vector<float> vector1, vector<float> vector2);

int main() {

	static const float arr1[] = {17.0, 10.0, 31.0, 5.0, 7.0};
	static const float arr2[] = {3.0, 1.0, 6.0, 19.0, 8.0};
	vector<float> v1 (arr1, arr1 + sizeof(arr1) / sizeof(arr1[0]));
	vector<float> v2 (arr2, arr2 + sizeof(arr2) / sizeof(arr2[0]));
	vector<float> v3 (v1.size());

	v3 = vectormultiply(v1, v2);

	for (int i = 0; i < v3.size(); i++) {
		cout << v3[i] << " ";
	}

	cout << endl;

	return 0;
}

vector<float> vectormultiply(vector<float> vector1, vector<float> vector2) {

	vector<float> vectorsum (vector1.size());

	for (int i = 0; i < vector1.size(); i++) {
		vectorsum[i] = vector1[i] * vector2[i];
	}

	return vectorsum;
}
