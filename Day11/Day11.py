''' 
=============== Advent Day 11 ===============

Each line gives the name of a device followed by a list of the devices to which its outputs are attached. 
So, bbb: ddd eee means that device bbb has two outputs, one leading to device ddd and the other leading to device eee.
The Elves are pretty sure that the issue isn't due to any specific device, but rather that the issue is triggered by data following some specific path through the devices. 
Data only ever flows from a device through its outputs; it can't flow backwards.

To help the Elves figure out which path is causing the issue, they need you to find every path from you to out.
How many different paths lead from you to out?

============================================
'''

class Solution:
    def __init__(self):
        pass

    def process_input(self, input):
        graph = {}
        key = ''
        keys = []

        for char in input:
            
            if char == ":":
                main_key = key
                key = ''
            
            elif char == " ":
                if key:
                    keys.append(key)
                    key = ''

            elif char == "\n":
                if key:
                    keys.append(key)
                graph[main_key] = keys
                keys = []
                key = ''

            else:
                key += char
        
        # Handle final line
        if keys:
            if key:
                keys.append(key)
            graph[main_key] = keys
        
        return graph

    def find_all_paths(self, graph, start, end, visited):

        if start == end:
            return visited
        
        if start not in graph:
            return visited
        
        for node in graph[start]:
            if node not in visited:
                visited.add(node)
                new_visited = self.find_all_paths(graph, node, end, visited)

        return new_visited

    def day_11(self, input):
        graph = self.process_input(input)
        start = 'svr'
        visited = {tuple(start)}
        paths = self.find_all_paths(graph, start, 'out', visited)
        return len(paths)


if __name__ == "__main__":
    filename  = "Day11/input.txt"
    with open(filename, "r") as f:
        input = f.read()
    solver = Solution()
    result = solver.day_11(input)
    print(f"Day 11 solution: {result}")