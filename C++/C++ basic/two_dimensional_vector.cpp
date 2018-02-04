#include <iostream>
#include <vector>

using namespace std;

vector < vector <int> > matrixsum(vector < vector <int> > matrix1, vector < vector <int> > matrix2);
void matrixprint(vector < vector <int> > inputmatrix);

int main() {

	vector < vector <int> > matrix1 (5, vector <int> (3, 2));
	vector < vector <int> > matrix2 (5, vector <int> (3, 26));

	vector < vector <int> > matrixresult;

	matrixresult = matrixsum(matrix1, matrix2);

	matrixprint(matrixresult);

	return 0;
}

vector < vector <int> > matrixsum(vector < vector <int> > matrix1, vector < vector <int> > matrix2) {

	vector < vector <int> > matrixsumresult (matrix1.size(), vector <int> (matrix1[0].size(), 0));

	for (int row = 0; row < matrix1.size(); row++) {
		for (int column = 0; column < matrix2.size(); column++) {
			matrixsumresult[row][column] = matrix1[row][column] + matrix2[row][column];
		}
  }

	return matrixsumresult;
}

void matrixprint(vector < vector <int> > inputmatrix) {

	for (int row = 0; row < inputmatrix.size(); row++) {
		for (int column = 0; column < inputmatrix[0].size(); column++) {
			cout << inputmatrix[row][column] << " ";
		}
		cout << endl;
  }
}
