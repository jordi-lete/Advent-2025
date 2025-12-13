'''
=============== Advent Day 6 ===============

Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

Here's the example worksheet again:

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  

Reading the problems right-to-left one column at a time, the problems are now quite different:

The rightmost problem is 4 + 431 + 623 = 1058
The second problem from the right is 175 * 581 * 32 = 3253600
The third problem from the right is 8 + 248 + 369 = 625
Finally, the leftmost problem is 356 * 24 * 1 = 8544

What is the grand total found by adding together all of the answers to the individual problems?

============================================
'''

class Solution:
    def __init__(self):
        self.grand_total = 0


    def process_input(self, input):
        
        # ================================
        # First split the data into rows
        # ================================
        rows = []
        row = ''

        for char in input:
            if char == "\n": # new row
                rows.append(row)
                # reset variables for new row
                row = ''
            else:
                row += char

        if row:
            rows.append(row)

        # ==================================================================
        # Split the data into problems and get the numbers from the columns
        # ==================================================================
        problem = [[]]
        index = 0
        for i in range(len(rows[0])):
            # Skip last row as that is the operator row
            number = ''
            for unit in range(len(rows) - 1):
                value = rows[unit][i]
                number += value

            # If the entrire column was blank then we move to the next problem
            if number == ' ' * (len(rows) - 1):
                index += 1
                problem.append([])
            else:
                problem[index].append(number)
                
        operators = []
        for char in rows[-1]:
            if char == " ":
                continue
            else:
                operators.append(char)

        return problem, operators
    
    
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


    def do_math(self, problem, operators):
        num_problems = len(problem)

        for i in range(num_problems):
            num_values = len(problem[i])
            operator = operators[i]
            # initialise with last value (work right to left)
            sol = int(problem[i][-1])

            # we work from right to left so start at index -2
            for row in range(2, num_values+1):
                sol = self.operate(operator, sol, int(problem[i][-row]))
            
            # Add result from each problem to the total
            self.grand_total += sol


    def day_6(self, input) -> int:
        problem, operators = self.process_input(input)
        self.do_math(problem, operators)
        return self.grand_total
            

if __name__ == "__main__":
    filename = "Day6/input.txt"
    with open(filename, "r") as f:
        input = f.read()
    solver = Solution()
    result = solver.day_6(input)
    print(f"Day 6 solution is: {result}")
    