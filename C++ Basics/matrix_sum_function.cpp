//TODO: Write a function that receives two integer matrices and outputs
// the sum of the two matrices. Then in your main() function, input a few
// examples to check your solution. Output the results of your function to 
// cout. You could even write a separate function that prints an arbitrarily 
// sized matric to cout.

#include<iostream>
#include<vector>
using namespace std;

vector < vector <int> > matrixsum(vector <vector <int> > matrix1,vector <vector <int> > matrix2);
void matrixprint(vector < vector <int> > inputmatrix);

int main(){
    // declare two matrices
    vector < vector <int> > matrix1(5, vector <int> (3,8));
    vector < vector <int> > matrix2(5,vector <int> (3,18));
    
    // create a matrix to store the sumation value
    vector < vector <int> > matrixresult;
    
    // calculate the sum of the two matrices
    matrixresult = matrixsum(matrix1,matrix2);
    
    // printing the matrix
    matrixprint(matrixresult);
    
    return 0;
}

// function to add two matrices together
vector < vector <int> > matrixsum(vector <vector <int> > matrix1,vector <vector <int> > matrix2){

    // declare a matrix with the same size as matrix1 and matrix2
    vector < vector <int> > matrixsumresult(matrix1.size(), vector <int> (matrix1[0].size(),0));

    // iterate through matrix1 and assign the sum of each element to the results matrix
    for (int row=0; row < matrix1.size(); row++){
        for (int col=0; col < matrix1[0].size(); col++){
            matrixsumresult[row][col]=matrix1[row][col] + matrix2[row][col];
        }
    }
    return matrixsumresult;
}

// function to print an integer matrix
void matrixprint(vector < vector <int> > inputmatrix) {

	for (int row = 0; row < inputmatrix.size(); row++) {
		for (int column = 0; column < inputmatrix[0].size(); column++) {
			cout << inputmatrix[row][column] << " ";
		}
		cout << endl;

	}
}

