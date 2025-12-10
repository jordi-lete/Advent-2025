'''
=============== Advent Day 4 ===============

Once a roll of paper can be accessed by a forklift, it can be removed. 
Once a roll of paper is removed, the forklifts might be able to access more rolls of paper, which they might also be able to remove. 
How many total rolls of paper could the Elves remove if they keep repeating this process?

============================================
'''

class Solution:
    def __init__(self):
        self.accessible_rolls = 0
        self.paper_removed = True


    def process_input(self, input):
        # Put the data into an array
        row = []
        grid = []
        for box in input:
            if box == "\n":
                grid.append(row)
                row = []
                continue
            row.append(box)
        
        # Handle final row
        if row:
            grid.append(row)
        
        return grid


    def check_boxes(self, grid):
        while self.paper_removed:
            num_removed = 0
            for i, row in enumerate(grid):
                for j, item in enumerate(row):
                    if item != '@':
                        continue

                    count = 0
                    if i > 0 and j > 0 and grid[i-1][j-1] == '@':
                        count += 1
                    if i > 0 and grid[i-1][j] == '@':
                        count += 1
                    if i > 0 and j < len(row)-1 and grid[i-1][j+1] == '@':
                        count += 1
                    if j > 0 and grid[i][j-1] == '@':
                        count += 1
                    if j < len(row)-1 and grid[i][j+1] == '@':
                        count += 1
                    if i < len(grid)-1 and j > 0 and grid[i+1][j-1] == '@':
                        count += 1
                    if i < len(grid)-1 and grid[i+1][j] == '@':
                        count += 1
                    if i < len(grid)-1 and j < len(row)-1 and grid[i+1][j+1] == '@':
                        count += 1
                    
                    if count < 4:
                        self.accessible_rolls += 1
                        grid[i][j] = '.'
                        num_removed += 1
            
            # if no paper was removed after checking the whole grid then exit
            if num_removed == 0:
                self.paper_removed = False


    def day_4(self, input):
        grid = self.process_input(input)
        self.check_boxes(grid)
        return self.accessible_rolls
            

if __name__ == "__main__":
    filename = "Day4/input.txt"
    with open(filename, "r") as f:
        input = f.read()
    solver = Solution()
    result = solver.day_4(input)
    print(f"Day 4 solution is: {result}")