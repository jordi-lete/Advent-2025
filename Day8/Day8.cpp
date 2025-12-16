/*

This list describes the position of 20 junction boxes, one per line. Each position is given as X,Y,Z coordinates. So, the first junction box in the list is at X=162, Y=817, Z=812.
To save on string lights, the Elves would like to focus on connecting pairs of junction boxes that are as close together as possible according to straight-line distance. 
In this example, the two junction boxes which are closest together are 162,817,812 and 425,690,689.
By connecting these two junction boxes together, because electricity can flow between them, they become part of the same circuit. 
After connecting them, there is a single circuit which contains two junction boxes, and the remaining 18 junction boxes remain in their own individual circuits.
The next two junction boxes to connect are 906,360,560 and 805,96,715. 
After connecting them, there is a circuit containing 3 junction boxes, a circuit containing 2 junction boxes, and 15 circuits which contain one junction box each.
The next two junction boxes are 431,825,988 and 425,690,689. Because these two junction boxes were already in the same circuit, nothing happens!
This process continues for a while, and the Elves are concerned that they don't have enough extension cables for all these circuits. 
They would like to know how big the circuits will be.
After making the ten shortest connections, there are 11 circuits: one circuit which contains 5 junction boxes, one circuit which contains 4 junction boxes, two circuits which contain 2 junction boxes each, and seven circuits which each contain a single junction box. 
Multiplying together the sizes of the three largest circuits (5, 4, and one of the circuits of size 2) produces 40.
Your list contains many junction boxes; connect together the 1000 pairs of junction boxes which are closest together. 
Afterward, what do you get if you multiply together the sizes of the three largest circuits?

*/

#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

struct Coord 
{
    int x;
    int y;
    int z;
};

struct Edges
{
    int i;
    int j;
    double dist;
};

class Solution 
{
    private:
        int m_connections = 0;

    public:
        Solution()
        {
            std::ifstream file("input.txt");
            if (!file)
            {
                std::cerr << "Failed to open input.txt\n";
            }

            std::vector<Coord> Coords;
            std::string line;

            while (std::getline(file, line))
            {
                long x, y, z;
                char comma;
                std::stringstream ss(line);
                // String format: x,y,z
                ss >> x >> comma >> y >> comma >> z;
                Coords.push_back({x, y, z});
            }

            // Get a list of potential connections and their distances
            std::vector<Edges> edges = getDists(Coords);
            
            // Sort the list into ascending order based on distance
            std::sort(edges.begin(), edges.end(), [](const Edges &a, const Edges &b) { return a.dist < b.dist; });

            // Now need to create the links
            std::vector<std::vector<int>> links = getLinks(edges, Coords.size());

            // sort the links by the number of elements in the circuit
            std::sort(links.begin(), links.end(), [](const std::vector<int> &a, const std::vector<int> &b) { return a.size() > b.size(); });

            std::cout << links[0].size() << std::endl;
            if (links.size() >= 3)
            {
                // Result is the number of elements in the 3 longest chains multiplied together
                int result = links[0].size() * links[1].size() * links[2].size();

                std::cout << links[0].size() << ", " << links[1].size() << ", " << links[2].size() << std::endl;
                std::cout << "Day8 result: " << result << std::endl;
            }
        }

        std::vector<std::vector<int>> getLinks(std::vector<Edges>& edges, const int numCoords)
        {
            std::vector<std::vector<int>> links;

            for (int edgeIdx = 0; edgeIdx < std::min(1000, (int)edges.size()); edgeIdx++)
            {
                auto& edge = edges[edgeIdx];

                int c_i = findInArray(edge.i, links);
                int c_j = findInArray(edge.j, links);

                if (c_i == -1 && c_j == -1)
                {
                    // New connection
                    links.push_back({edge.i, edge.j});
                    m_connections++;
                }
                else if (c_i > -1 && c_j == -1)
                {
                    links[c_i].push_back(edge.j);
                    m_connections++;
                }
                else if (c_j > -1 && c_i == -1)
                {
                    links[c_j].push_back(edge.i);
                    m_connections++;
                }
                else if (c_i > -1 && c_j > -1)
                {
                    if (c_i != c_j)
                    {
                        if (c_i < c_j)
                        {
                            // Both in existing circuits so merge the circuits
                            links[c_i].insert(links[c_i].end(), links[c_j].begin(), links[c_j].end());
                            // Remove the old circuit
                            links.erase(links.begin() + c_j);
                        }
                        else
                        {
                            links[c_j].insert(links[c_j].end(), links[c_i].begin(), links[c_i].end());
                            links.erase(links.begin() + c_i);
                        }
                        m_connections++;
                    }
                }
            }
            return links;
        }

        int findInArray(int index, const std::vector<std::vector<int>>& links)
        {
            for (int i = 0; i < links.size(); i++)
            {
                if (std::find(links[i].begin(), links[i].end(), index) != links[i].end())
                {
                    return i;
                }
            }
            return -1;
        }

        std::vector<Edges> getDists(std::vector<Coord>& Coords)
        {
            std::vector<Edges> edges;

            for (int i = 0; i < Coords.size() - 1; i++)
            {
                Coord c1 = Coords[i];
                for (int j = i+1; j < Coords.size(); j++)
                {
                    Coord c2 = Coords[j];
                    double dist = euclideanDistance(c1, c2);
                    edges.push_back({i, j, dist});
                }
            }
            return edges;
        }

        double euclideanDistance(Coord p, Coord q)
        {
            double dx = p.x - q.x;
            double dy = p.y - q.y;
            double dz = p.z - q.z;
            return std::sqrt(dx*dx + dy*dy + dz*dz);
        }

};

int main()
{
    Solution solver;
    return 0;
}