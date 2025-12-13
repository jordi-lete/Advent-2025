'''
=============== Advent Day 6 ===============

the problems are arranged a little strangely; they seem to be presented next to each other in a very long horizontal list. For example:

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  

Each problem's numbers are arranged vertically; at the bottom of the problem is the symbol for the operation that needs to be performed. Problems are separated by a full column of only spaces. 
The left/right alignment of numbers within each problem can be ignored.
So, this worksheet contains four problems:

123 * 45 * 6 = 33210
328 + 64 + 98 = 490
51 * 387 * 215 = 4243455
64 + 23 + 314 = 401

To check their work, cephalopod students are given the grand total of adding together all of the answers to the individual problems.
What is the grand total found by adding together all of the answers to the individual problems?

============================================
'''

class Solution:
    def __init__(self):
        self.grand_total = 0


    def process_input(self, input):
        # create array for each row in input
        row = []
        problem = []
        value = ''

        for char in input:
            if char == "\n": # new row
                if value:
                    row.append(value)
                problem.append(row)
                # reset variables for new row
                value = ''
                row = []
            elif char == " ":
                if value:
                    row.append(value)
                value = ''
                continue
            else:
                value += char

        if row:
            if value:
                row.append(value)
            problem.append(row)

        return problem
    
    
    def operate(self, operator, a, b) -> int:
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        else:
            print(f"unexpected operator: {operator}, defaulting to +")
            return a + b


    def do_math(self, problem):
        num_problems = len(problem[0])
        rows = len(problem)

        for i in range(num_problems):
            operator = problem[-1][i]
            # initialise with value in first row
            sol = int(problem[0][i])

            # start from second row as we have have already initialised with first row 
            for row in range(1, rows - 1):
                sol = self.operate(operator, sol, int(problem[row][i]))
            
            # Add result from each problem to the total
            self.grand_total += sol


    def day_6(self, input) -> int:
        problem = self.process_input(input)
        self.do_math(problem)
        return self.grand_total
            

if __name__ == "__main__":
    filename = "Day6/input.txt"
    with open(filename, "r") as f:
        input = f.read()
    solver = Solution()
    result = solver.day_6(input)
    print(f"Day 6 solution is: {result}")
    