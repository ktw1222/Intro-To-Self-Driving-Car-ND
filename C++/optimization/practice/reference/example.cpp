#include <iostream>
#include <vector>

using namespace std;

void matrix_address(vector< vector<int> > my_matrix);

int main() {

    vector< vector<int> > matrix(5, vector<int>(6,2));

    cout << "original variable address: " << &matrix << "\n";

    matrix_address(matrix);

    return 0;
}

void matrix_address(vector< vector<int> > my_matrix) {

    cout << "function variable address: " << &my_matrix << "\n";

}

// original variable address: 0x7fff5fbff650

// function variable address: 0x7fff5fbff608
