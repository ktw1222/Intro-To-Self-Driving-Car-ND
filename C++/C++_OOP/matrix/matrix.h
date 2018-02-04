#ifndef MATRIX_H
#define MATRIX_H

#include <vector>
#include <stdexcept> //library for the invalid_argument method
#include <iostream>

class Matrix
{

        private:

            std::vector< std::vector<float> > grid;
            std::vector<int>::size_type rows;
            std::vector<int>::size_type cols;

        public:

        // constructor function declarations
            // An empty constructor function
            Matrix ();
            // A constructor function that accepts a 2-dimensional vector
            Matrix (std::vector< std::vector<float> >);

        // set and get function declarations
            void setGrid(std::vector< std::vector<float> >);

            // getGrid returns a 2-D vector and has no input
            std::vector< std::vector<float> > getGrid();
            // getRows returns a size_type and has no input
            std::vector<int>::size_type getRows();
            // get Cols returns a size_type and has no input
            std::vector<int>::size_type getCols();

        // matrix function declarations
            // matrix_transpose has no input and outputs a 2D vector
            Matrix matrix_transpose();
            // matrix_addition receives a Matrix and outputs a 2D vector
            Matrix matrix_addition(Matrix);
            // matrix_print has no inputs and no outputs
            void matrix_print();

};

#endif /* MATRIX_H */
