/*
=============== Advent Day 5 ===============

You quickly locate a diagram of the tachyon manifold (your puzzle input). 
A tachyon beam enters the manifold at the location marked S; tachyon beams always move downward. 
Tachyon beams pass freely through empty space (.). 
However, if a tachyon beam encounters a splitter (^), the beam is stopped; instead, a new tachyon beam continues from the immediate left and from the immediate right of the splitter.
Analyze your manifold diagram. How many times will the beam be split?

============================================
*/ 

#include <iostream>
#include <fstream>
#include <sstream>

#include <string>
#include <vector>

class Solution
{
    private:
        int m_numSplits = 0;

    public:
        Solution()
        {
            std::ifstream file("input.txt");
            if (!file) 
            {
                std::cerr << "Failed to open input.txt\n";
            }

            std::string line;
            std::string beams;
            bool firstLine = true;

            // Loop for each line in file
            while (std::getline(file, line)) 
            {
                if (firstLine) 
                {
                    beams = line;
                    for (int i = 0; i < line.size(); i++) 
                    {
                        if (line[i] == 'S')
                        {
                            beams[i] = '|';
                        }
                    }
                    firstLine = false;
                    continue;
                }

                beams = processBeamLine(beams, line);
            }

            std::cout << "Day7 solution: " << m_numSplits << std::endl;
        }

        std::string processBeamLine(std::string incoming, std::string layout)
        {
            int numCells = incoming.length();
            if (numCells != layout.length()) 
            {
                std::cout << "input does not match length of next";
            }

            std::string newLine = layout;

            for (int i=0; i<numCells; i++)
            {
                if (incoming[i] == '|' && layout[i] == '.') 
                {
                    newLine[i] = '|';
                }
                else if (incoming[i] == '|' && layout[i] == '^') 
                {
                    if (i > 0)              newLine[i-1] = '|';
                    if (i < numCells - 1)   newLine[i+1] = '|';
                    m_numSplits++;
                }
            }
            return newLine;
        }
};


int main()
{
    Solution solution;
    return 0;
}
