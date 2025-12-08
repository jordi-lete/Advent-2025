''' 
=============== Advent Day 1 ===============

You remember from the training seminar that "method 0x434C49434B" means you're actually supposed to count the 
number of times any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one.

============================================
'''
import math

class Solution:
    def process_input(self, input):
        entry = ''
        entries = []
        for char in input:
            if char == "\n":
                entries.append(entry)
                entry = ''
                continue
            entry += char

        # Handle final entry of input (no newline)
        if entry:
            entries.append(entry)

        return entries

    def run_combination(self, input, value) -> int:
        zerod_count = 0
        for entry in input:
            if entry[0] == 'R':
                change = int(entry[1:])
                zerod_count += math.floor((value + change) / 100)
                value = (value + change) % 100
            elif entry[0] == 'L':
                change = int(entry[1:])
                zerod_count += abs(math.ceil(((value - change) / 100) - 1)) # -1 because we don't want to add 1 when it doesn't pass zero at all
                if value == 0:
                    zerod_count -= 1
                value = (value - change) % 100

            else:
                print(f"Error: Entries should only start with R or L but you have: {entry}")

        return zerod_count

    def day_1(self, input) -> int:
        entries = self.process_input(input)
        value = 50
        return self.run_combination(entries, value)
        

if __name__ == "__main__":
    filename  = "Day1/input.txt"
    with open(filename, "r") as f:
        input = f.read()
    solver = Solution()
    result = solver.day_1(input)
    print(f"Today's solution: {result}")