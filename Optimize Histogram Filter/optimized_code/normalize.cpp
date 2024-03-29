#include "headers/normalize.h"
using namespace std;

// OPTIMIZATION: Pass variable by reference
vector< vector<float> > normalize(vector< vector <float> > &grid) {

  	// OPTIMIZATION: Avoid declaring and defining 				// intermediate variables that are not needed.
	float total = 0.0;
	
	vector<float> row;
	vector<float> newRow;
	float oldProb;
	for (int i = 0; i < grid.size(); i++)
	{
		row = grid[i];
		for (int j=0; j< row.size(); j++)
		{
			oldProb = row[j];
			total += oldProb;
		}
	}

	vector< vector<float> > newGrid;

	for (int i = 0; i < grid.size(); i++) {
		vector<float> row = grid[i];
		newRow.clear();
		for (int j=0; j< row.size(); j++) {
			float oldProb = row[j];
			float newProb = oldProb / total;
			newRow.push_back(newProb);
		}
		newGrid.push_back(newRow);
	}

	return newGrid;
}
