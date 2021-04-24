#include "headers/initialize_beliefs.h"

using namespace std;

// OPTIMIZATION: pass large variables by reference
vector< vector <float> > initialize_beliefs(int height, int width) {
	float prob_per_cell = 1.0 / float(height * width);
	// OPTIMIZATION: Which of these variables are necessary?
	// OPTIMIZATION: Reserve space in memory for vectors
  	vector< vector <float> > newGrid;
	vector<float> row;
  	newGrid.reserve(height);
  	row.reserve(width);
	//int i, j, height, width, area;
	//float total, prob_per_cell;

	//height = grid.size();
	//width = grid[0].size();
 
	//area = height * width;

  	//prob_per_cell = 1.0 / ( height * width) ;

  	// OPTIMIZATION: Is there a way to get the same results 	// without nested for loops?
	for (int i = 0; i < width; i++) {
		row.push_back(prob_per_cell);
	}

	for (int i = 0; i < height; i++) {
		newGrid.push_back(row);
	}
	return newGrid;
}