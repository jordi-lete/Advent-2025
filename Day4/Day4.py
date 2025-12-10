'''
=============== Advent Day 4 ===============

The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.
For example:

..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@


The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions. 
If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.
Consider your complete diagram of the paper roll locations. How many rolls of paper can be accessed by a forklift?

============================================
'''

class Solution:
    def __init__(self):
        self.accessible_rolls = 0


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