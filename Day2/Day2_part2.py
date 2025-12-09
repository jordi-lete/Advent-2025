'''
=============== Advent Day 2 ===============

Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice.
So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.

============================================
'''

class Solution:
    def __init__(self):
        self.score = 0

    def process_file(self, input):
        value = ''
        entries = []

        for char in input:
            if char == "-":
                start_val = value
                value = ''
                continue

            elif char == ",":
                end_val = value
                value = ''
                entries.append([start_val, end_val])
                continue

            value += char
        
        # Hit the final entry from input (since no , at the end)
        if value != '':
            end_val = value
            entries.append([start_val, end_val])

        return entries
    
    def get_factors(self, num):
        # get factors of the number length as these are possible splits
        num_length = len(num)
        factors = []
        for i in range(2, num_length+1):
            if num_length % i == 0:
                factors.append(i)
        return factors
    
    def test_value(self, value):
        factors = self.get_factors(value)

        # for each factor check if all subsets of that length are equal
        for f in factors:
            valid = True
            subset = len(value) // f
            part1 = value[:subset]

            for i in range(1,f):
                partx = value[subset*i : subset*(i+1)]
                if part1 != partx:
                    valid = False
                    break

            # if we get to the end of the loop without breaking then it is a valid result
            if valid:
                return True
            
        return False
    
    def run_experiment(self, entries):
        for entry in entries:

            start = int(entry[0])
            end = int(entry[1])

            for i in range(start, end+1):
                value = str(i)

                valid = self.test_value(value)

                if valid:
                    self.score += i

        return self.score
            
    def day_2(self, input) -> int:
        entries = self.process_file(input)
        score = self.run_experiment(entries)
        return score
        

if __name__ == "__main__":
    filename = "Day2/input.txt"
    with open(filename, "r") as f:
        input = f.read()
    solver = Solution()
    result = solver.day_2(input)
    print(f"Day 2 solution is: {result}")
