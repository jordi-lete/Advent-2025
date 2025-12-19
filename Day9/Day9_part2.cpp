/*
Advent of Code Day 9 part 2:
The Elves just remembered: they can only switch out tiles that are red or green. So, your rectangle can only include red or green tiles.
In your list, every red tile is connected to the red tile before and after it by a straight line of green tiles. 
The list wraps, so the first red tile is also connected to the last red tile. Tiles that are adjacent in your list will always be on either the same row or the same column.
Using the same example as before, the tiles marked X would be green:

..............
.......#XXX#..
.......X...X..
..#XXXX#...X..
..X........X..
..#XXXXXX#.X..
.........X.X..
.........#X#..
..............

In addition, all of the tiles inside this loop of red and green tiles are also green. So, in this example, these are the green tiles:

..............
.......#XXX#..
.......XXXXX..
..#XXXX#XXXX..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............

The remaining tiles are never red nor green.
The rectangle you choose still must have red tiles in opposite corners, but any other tiles it includes must now be red or green. This significantly limits your options.
For example, you could make a rectangle out of red and green tiles with an area of 15 between 7,3 and 11,1:

..............
.......OOOOO..
.......OOOOO..
..#XXXXOOOOO..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............

Using two red tiles as opposite corners, what is the largest area of any rectangle you can make using only red and green tiles?
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <unordered_map>

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

    void checkCoords(const std::vector<Coord>& redCoords, const std::unordered_map<long long, std::pair<long long, long long>>& rowBounds);
};

Solution::Solution()
{
    std::ifstream file("input.txt");
    if (!file) 
    {
        std::cerr << "Failed to open input.txt\n";
        return;
    }

    std::string line;
    std::vector<Coord> redCoords;

    // process the red tiles
    while (std::getline(file, line))
    {
        std::stringstream ss(line);
        long long x, y;
        char comma;
        ss >> x >> comma >> y;
        redCoords.push_back({x, y});
    }

    // Build boundary tiles (red + exterior green)
    std::vector<Coord> boundary;
    for (size_t i = 0; i < redCoords.size(); i++)
    {
        Coord c1 = redCoords[i];
        Coord c2 = redCoords[(i + 1) % redCoords.size()]; // wrap

        if (c1.x == c2.x)
        {
            long long y1 = std::min(c1.y, c2.y);
            long long y2 = std::max(c1.y, c2.y);
            for (long long y = y1; y <= y2; y++)
                boundary.push_back({c1.x, y});
        }
        else if (c1.y == c2.y)
        {
            long long x1 = std::min(c1.x, c2.x);
            long long x2 = std::max(c1.x, c2.x);
            for (long long x = x1; x <= x2; x++)
                boundary.push_back({x, c1.y});
        }
    }

    // Precompute row bounds (minX, maxX) for each y
    // Any rectangle that includes this row must have its x-range fully inside [minX, maxX]
    std::unordered_map<long long, std::pair<long long, long long>> rowBounds;
    for (const auto& c : boundary)
    {
        auto it = rowBounds.find(c.y);
        if (it == rowBounds.end())
            rowBounds[c.y] = {c.x, c.x};
        else
        {
            it->second.first = std::min(it->second.first, c.x);
            it->second.second = std::max(it->second.second, c.x);
        }
    }

    checkCoords(redCoords, rowBounds);

    std::cout << "Day 9 solution: " << m_maxArea << std::endl;
}

void Solution::checkCoords(const std::vector<Coord>& redCoords, const std::unordered_map<long long, std::pair<long long, long long>>& rowBounds)
{
    for (size_t i = 0; i < redCoords.size(); i++)
    {
        const Coord& c1 = redCoords[i];
        for (size_t j = i + 1; j < redCoords.size(); j++)
        {
            const Coord& c2 = redCoords[j];

            // Contruct rectangle
            long long minX = std::min(c1.x, c2.x);
            long long maxX = std::max(c1.x, c2.x);
            long long minY = std::min(c1.y, c2.y);
            long long maxY = std::max(c1.y, c2.y);

            bool valid = true;
            for (long long y = minY; y <= maxY; y++)
            {
                auto it = rowBounds.find(y);
                // if y not in bounds or x < minx or x > maxX
                if (it == rowBounds.end() || minX < it->second.first || maxX > it->second.second)
                {
                    valid = false;
                    break;
                }
            }

            if (valid)
            {
                long long area = (maxX - minX + 1) * (maxY - minY + 1);
                m_maxArea = std::max(m_maxArea, area);
            }
        }
    }
}

int main()
{
    Solution solver;
    return 0;
}