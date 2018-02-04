#include "headers/initialize_beliefs.h"

using namespace std;

vector< vector <float> > initialize_beliefs(int height, int width) {

	float prob_per_cell = 1.0 / float(height * width);

	vector<float> row;
	vector< vector<float> > newGrid;

	row.reserve(width);
	newGrid.reserve(height);

	for (int i = 0; i < width; i++) {
		row.push_back(prob_per_cell);
	}

	for (int i = 0; i < height; i++) {
		newGrid.push_back(row);
	}

	return newGrid;
}
