#include "headers/move.h"
#include "headers/zeros.h"

using namespace std;

// OPTIMIZATION: Pass large variable by reference
vector< vector <float> > move(int dy, int dx, 
	vector < vector <float> > &beliefs) 
{
	
	int height = beliefs.size();
	int width = beliefs[0].size();

	float belief;
	vector < vector <float> > newGrid = zeros(height,width);
  
  	// OPTIMIZATION: Use improved zeros function
	//newGrid = zeros(height, width);

// OPTIMIZATION: Eliminate any variables that aren't needed
	//vector <float> row, newRow;
	//int i, j, new_i, new_j;
	
  	for (int i=0; i<height; i++) {
		for (int j=0; j<width; j++) {
			float new_i = (i + dy + height) % height;
			float new_j = (j + dx + width)  % width;
			belief = beliefs[i][j];

			newGrid[new_i][new_j] = belief;
		}
	}
	return newGrid;
}
