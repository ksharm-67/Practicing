#include <iostream>
#include <cmath>

//Check if the given number is a power of 3 or not
bool isPowerOfThree(int n) {
    if (n <= 0) return false;

    double num = log10(n) / log10(3);
    
    return (floor(num) == num) && (ceil(num) == num));
}