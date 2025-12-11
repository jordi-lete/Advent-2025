/*
=============== Advent Day 5 ===============

So that they can stop bugging you when they get new inventory, the Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh.
An ingredient ID is still considered fresh if it is in any range.
Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:

3-5
10-14
16-20
12-18

The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. 
So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.
Process the database file again. How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?

============================================
*/ 

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

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
    }

    long long freshCount = 0;
    long long lower, upper;
    std::vector<Range> processedRanges;

    // Sort ranges by start - this avoids cases such as 100-200 followed by 50-250
    std::sort(ranges.begin(), ranges.end(),
        [](const Range& r1, const Range& r2) {
            return r1.start < r2.start;
        });

    for (auto range : ranges)
    {
        lower = range.start;
        upper = range.end;

        // Here I am adjusting the start/end value of the range if it has already been added
        // e.g. if we process 10-20 and then try 15-25 I am changing this to 10-20 and 21-25
        for (auto prange : processedRanges)
        {
            if (lower <= upper && lower >= prange.start && lower <= prange.end)
            {
                lower = prange.end + 1;
            }
            if (lower <= upper && upper >= prange.start && upper <= prange.end)
            {
                upper = prange.start - 1;
            }
        }

        if (lower <= upper)  // Only count if there's a valid range left
        {
            freshCount += upper - lower + 1;
        }
        processedRanges.push_back(range);
    }

    std::cout << "Day5 solution: " << freshCount << std::endl;
    return 1;
}
