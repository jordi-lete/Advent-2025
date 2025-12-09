'''
=============== Advent Day 3 ===============

There are batteries nearby that can supply emergency power to the escalator for just such an occasion. 
The batteries are each labeled with their joltage rating, a value from 1 to 9. 
You make a note of their joltage ratings (your puzzle input). For example:

987654321111111
811111111111119
234234234234278
818181911112111

The batteries are arranged into banks; each line of digits in your input corresponds to a single bank of batteries.
Within each bank, you need to turn on exactly two batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on. 
For example, if you have a bank like 12345 and you turn on batteries 2 and 4, the bank would produce 24 jolts. (You cannot rearrange batteries.)

You'll need to find the largest possible joltage each bank can produce.
The total output joltage is the sum of the maximum joltage from each bank, so in this example, the total output joltage is 98 + 89 + 78 + 92 = 357.

============================================
'''

class Solution:
    def __init__(self):
        self.total = 0

    def process_input(self, input):
        battery = ''
        pack = []

        for char in input:
            if char == '\n':
                pack.append(battery)
                battery = ''
                continue
            battery += char

        # Handle case of final row (no \n for final row)
        if battery:
            pack.append(battery)

        return pack
    
    def get_max_joltage(self, battery):
        max = '0'
        # first pass - we want to maximise the tens unit but don't consider the very last entry for tens unit
        for i, charge in enumerate(battery[:-1]):
            if int(charge) > int(max):
                max = charge
                index = i

        second = '0'
        for j in range(index+1, len(battery)):
            if int(battery[j]) > int(second):
                second = battery[j]

        joltage = int(max + second)
        return joltage

    def day_3(self, input):
        pack = self.process_input(input)
        for battery in pack:
            self.total += self.get_max_joltage(battery)
        return self.total
            

if __name__ == "__main__":
    filename = "Day3/input.txt"
    with open(filename, "r") as f:
        input = f.read()
    solver = Solution()
    result = solver.day_3(input)
    print(f"Day 3 solution is: {result}")