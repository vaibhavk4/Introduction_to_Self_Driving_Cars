#include "headers/blur.h"
#include "headers/zeros.h"
using namespace std;

// OPTIMIZATION: Pass large variable by reference
vector < vector <float> > blur(vector < vector < float> > &grid) {

	// OPTIMIZATION: window, DX and  DY variables have the 
    // same value each time the function is run.
  	// It's very inefficient to recalculate the vectors
    // every time the function runs. 
    // 
    // The const and/or static operator could be useful.
  	// Define and declare window, DX, and DY using the
    // bracket syntax: vector<int> foo = {1, 2, 3, 4} 
    // instead of calculating these vectors with for loops 
    // and push back
  	static float Global_blurring = 0.12;

	static float center = 1.0 - Global_blurring;
	static float corner = Global_blurring / 12.0;
	static float adjacent = Global_blurring / 6.0;

	static vector <int> DX = {-1,0,1};
	static vector <int> DY = {-1,0,1};

  	static vector< vector <float>> Global_Window = {{corner,adjacent,corner},{adjacent,center,adjacent},{corner,adjacent,corner}};
	
  	vector<vector <float>> newGrid;
  	vector <float> row;
  	vector <float> newRow;

	int dx,dy;
	int ii,jj,new_i,new_j;
	
  	int height = grid.size(); 
	int width = grid[0].size();
	// OPTIMIZATION: Use your improved zeros function
  	newGrid = zeros(height,width);
	
  float newVal,multiplier;

	for (int i=0; i< height; i++ ) {
		for (int j=0; j<width; j++ ) {
			newVal = grid[i][j];
			
			for (ii=0; ii<3; ii++) {
				dy = DY[ii];
				for (jj=0; jj<3; jj++) {
					dx = DX[jj];
					new_i = (i + dy + height) % height;
					new_j = (j + dx + width) % width;
					multiplier = Global_Window[ii][jj];
					newGrid[new_i][new_j] += newVal * multiplier;
				}
			}
		}
	}

	return newGrid;
}
