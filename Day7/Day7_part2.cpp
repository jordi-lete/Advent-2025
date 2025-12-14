#include <iostream>
#include <fstream>
#include <string>
#include <vector>

class Solution
{
private:
    long long m_numSplits = 0;

public:
    Solution()
    {
        std::ifstream file("input.txt");
        if (!file)
        {
            std::cerr << "Failed to open input.txt\n";
            return;
        }

        std::string line;
        std::getline(file, line);

        int width = line.size();

        // dp[i] = number of beams at column i
        std::vector<long long> dp(width, 0);

        // initialise from first row
        for (int i = 0; i < width; i++)
        {
            if (line[i] == 'S')
                dp[i] = 1;
        }

        // process remaining rows
        while (std::getline(file, line))
        {
            std::vector<long long> next(width, 0);

            for (int i = 0; i < width; i++)
            {
                if (dp[i] == 0) continue;

                if (line[i] == '.')
                {
                    next[i] += dp[i];
                }
                else if (line[i] == '^')
                {
                    if (i > 0)
                        next[i - 1] += dp[i];
                    if (i < width - 1)
                        next[i + 1] += dp[i];

                    m_numSplits += dp[i];
                }
            }

            dp = std::move(next);
        }

        long long timelines = 0;
        for (long long x : dp) {
            timelines += x;
        }
        std::cout << "Day 7 solution: " << timelines << "\n";
    }
};

int main()
{
    Solution solution;
    return 0;
}
