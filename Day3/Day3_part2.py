'''
=============== Advent Day 3 ===============

Now, you need to make the largest joltage by turning on exactly twelve batteries within each bank.
The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; 
the only difference is that now there will be 12 digits in each bank's joltage output instead of two.

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
        index = 0
        joltage = ''
        last_index = 0 # We need this for keeping track of where we need to start in the list

        for i in range(12):
            max = '0'
            j = len(battery) - (12 - i)

            for i, charge in enumerate(battery[index:j+1]):
                if int(charge) > int(max):
                    max = charge
                    index = i + 1 + last_index

            last_index = index
            joltage += max

        return int(joltage)
    

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