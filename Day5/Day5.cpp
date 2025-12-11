/*
=============== Advent Day 5 ===============

The database operates on ingredient IDs. It consists of a list of fresh ingredient ID ranges, a blank line, and a list of available ingredient IDs. For example:

3-5
10-14
16-20
12-18

1
5
8
11
17
32

The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh. The ranges can also overlap; an ingredient ID is fresh if it is in any range.
The Elves are trying to determine which of the available ingredient IDs are fresh.

============================================
*/ 

#include <iostream>
#include <fstream>
#include <sstream>

#include <string>
#include <vector>

struct Range {
    long long start;
    long long end;
};

int main()
{
    std::ifstream file("input.txt");
    if (!file) {
        std::cerr << "Failed to open input.txt\n";
        return 1;
    }

    std::vector<Range> ranges;
    std::vector<long long> ids;

    std::string line;
    bool isRange = true;

    // Loop for each line in file
    while (std::getline(file, line)) 
    {
        if (line.empty()) {
            isRange = false;
            continue;
        }

        if (isRange)
        {
            // Format: "start-end"
            std::stringstream ss(line);
            long long start, end;
            char dash;
            ss >> start >> dash >> end;
            ranges.push_back({start, end});
        }
        else
        {
            // Reading an ingredient
            long long ingredient = std::stoll(line);
            ids.push_back(ingredient);
        }
    }

    int freshCount = 0;
    long long lower, upper;
    for (long long id : ids)
    {
        for (auto range : ranges)
        {
            lower = range.start;
            upper = range.end;
            if (id >= lower && id <= upper)
            {
                freshCount++;
                break;
            }
        }
    }

    std::cout << "Day5 solution: " << freshCount << std::endl;
    return 1;
}
