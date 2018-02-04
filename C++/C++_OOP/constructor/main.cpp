#include <iostream>
#include  "add.h"

int main() {

    Add adder(5);
    std::cout << adder.addition() << std::endl;
    return 0;

}
