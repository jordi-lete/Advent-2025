/*

The Elves were right; they definitely don't have enough extension cables. 
You'll need to keep connecting junction boxes together until they're all in one large circuit.
Continuing the above example, the first connection which causes all of the junction boxes to form a single circuit is between the junction boxes at 216,146,977 and 117,168,530. 
The Elves need to know how far those junction boxes are from the wall so they can pick the right extension cable; 
multiplying the X coordinates of those two junction boxes (216 and 117) produces 25272.
Continue connecting the closest unconnected pairs of junction boxes together until they're all in the same circuit. 
What do you get if you multiply together the X coordinates of the last two junction boxes you need to connect?

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
        int m_numCoords = 0;

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
            m_numCoords = Coords.size();

            // Get a list of potential connections and their distances
            std::vector<Edges> edges = getDists(Coords);
            
            // Sort the list into ascending order based on distance
            std::sort(edges.begin(), edges.end(), [](const Edges &a, const Edges &b) { return a.dist < b.dist; });

            // Get the final edge that is added to the circuit
            Edges lastConnectedEdge = getLinks(edges);
            long long result = (long long)Coords[lastConnectedEdge.i].x * (long long)Coords[lastConnectedEdge.j].x;
            std::cout << "Day8 part 2 result: " << result << std::endl;
        }

        Edges getLinks(std::vector<Edges>& edges)
        {
            std::vector<std::vector<int>> links;
            Edges lastEdge;

            for (auto& edge : edges)
            {
                int c_i = findInArray(edge.i, links);
                int c_j = findInArray(edge.j, links);

                bool added = false;

                if (c_i == -1 && c_j == -1) 
                {
                    links.push_back({edge.i, edge.j});
                    added = true;
                } 
                else if (c_i > -1 && c_j == -1) 
                {
                    links[c_i].push_back(edge.j);
                    added = true;
                } 
                else if (c_j > -1 && c_i == -1) 
                {
                    links[c_j].push_back(edge.i);
                    added = true;
                } 
                else if (c_i != c_j)
                { 
                    if (c_i < c_j) 
                    {
                        links[c_i].insert(links[c_i].end(), links[c_j].begin(), links[c_j].end());
                        links.erase(links.begin() + c_j);
                    } 
                    else 
                    {
                        links[c_j].insert(links[c_j].end(), links[c_i].begin(), links[c_i].end());
                        links.erase(links.begin() + c_i);
                    }
                    added = true;
                }

                if (added) 
                {
                    m_connections++;
                    lastEdge = edge;
                    if (m_connections == m_numCoords - 1) return lastEdge;
                }
            }
            return lastEdge;
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