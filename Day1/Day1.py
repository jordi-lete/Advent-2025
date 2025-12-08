''' 
=============== Advent Day 1 ===============

The safe has a dial with only an arrow on it; around the dial are the numbers 0 through 99 in order. As you turn the dial, it makes a small click noise as it reaches each number.
The attached document (your puzzle input) contains a sequence of rotations, one per line, which tell you how to open the safe. A rotation starts with an L or R which indicates whether the rotation should be to the left (toward lower numbers) or to the right (toward higher numbers). Then, the rotation has a distance value which indicates how many clicks the dial should be rotated in that direction.
So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19. After that, a rotation of L19 would cause it to point at 0.
Because the dial is a circle, turning the dial left from 0 one click makes it point at 99. Similarly, turning the dial right from 99 one click makes it point at 0.
So, if the dial were pointing at 5, a rotation of L10 would cause it to point at 95. After that, a rotation of R5 could cause it to point at 0.
The dial starts by pointing at 50.
You could follow the instructions, but your recent required official North Pole secret entrance security training seminar taught you that the safe is actually a decoy. The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.

============================================
'''

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
                value = (value + change) % 100
            elif entry[0] == 'L':
                change = int(entry[1:])
                value = (value - change) % 100
            else:
                print(f"Error: Entries should only start with R or L but you have: {entry}")

            if value == 0:
                zerod_count += 1

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