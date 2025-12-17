/*
Advent of Code Day 9:
The movie theater has a big tile floor with an interesting pattern. 
Elves here are redecorating the theater by switching out some of the square tiles in the big grid they form. 
Some of the tiles are red; the Elves would like to find the largest rectangle that uses red tiles for two of its opposite corners. 
They even have a list of where the red tiles are located in the grid (your puzzle input).
For example:

7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3

You can choose any two red tiles as the opposite corners of your rectangle; your goal is to find the largest rectangle possible.
For example, you could make a rectangle (shown as O) with an area of 24 between 2,5 and 9,7:

..............
.......#...#..
..............
..#....#......
..............
..OOOOOOOO....
..OOOOOOOO....
..OOOOOOOO.#..
..............

Using two red tiles as opposite corners, what is the largest area of any rectangle you can make?
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

struct Coord
{
    long long x;
    long long y;
};

class Solution
{
    private:
        long long m_maxArea = 0;
        
    public:
        Solution();

        void checkCoords(std::vector<Coord>& coords);
};

Solution::Solution()
{
    std::ifstream file("input.txt");
        if (!file) 
        {
            std::cerr << "Failed to open input.txt\n";
        }

    std::string line;
    std::vector<Coord> Coords;

    // process the input
    while (std::getline(file, line))
    {
        std::stringstream ss(line);
        long long x, y;
        char comma;
        ss >> x >> comma >> y;
        Coords.push_back({x, y});
    }
    std::cout << Coords.size() <<std::endl;

    checkCoords(Coords);

    std::cout << "Day 9 solution: " << m_maxArea << std::endl;
}

void Solution::checkCoords(std::vector<Coord>& coords)
{
    for (int i = 0; i < coords.size()-1; i++)
    {
        Coord c1 = coords[i];
        for (int j = i+1; j < coords.size(); j++)
        {
            Coord c2 = coords[j];
            long long dx = abs(c1.x - c2.x) + 1; // +1 as going from e.g. x=0 to x=10 is actually 11 steps
            long long dy = abs(c1.y - c2.y) + 1;
            long long area = dx * dy;
            if (area > m_maxArea)
            {
                m_maxArea = area;
            }
        }
    }
}

int main()
{
    Solution solver;
    return 0;
}