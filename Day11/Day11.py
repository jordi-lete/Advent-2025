''' 
=============== Advent Day 11 ===============


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

    def find_all_paths(self, graph, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]
        
        if start not in graph:
            return []
        
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = self.find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
                    
        return paths

    def day_11(self, input):
        graph = self.process_input(input)
        paths = self.find_all_paths(graph, 'you', 'out')
        return len(paths)


if __name__ == "__main__":
    filename  = "Day11/input.txt"
    with open(filename, "r") as f:
        input = f.read()
    solver = Solution()
    result = solver.day_11(input)
    print(f"Day 11 solution: {result}")