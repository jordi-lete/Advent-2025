'''
=============== Advent Day 2 ===============

The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).
Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence 
of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.
None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)
Your job is to find all of the invalid IDs that appear in the given ranges.

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
    
    def run_experiment(self, entries):
        for entry in entries:
            # Doesn't work for entries of odd length
            if len(entry[0]) == len(entry[1]) and (len(entry[0]) % 2 != 0):
                continue

            start = int(entry[0])
            end = int(entry[1])

            for i in range(start, end+1):
                value = str(i)

                # if odd length skip
                if (len(value) % 2) != 0:
                    continue

                halflength = len(value) // 2
                first_half = value[:halflength]
                second_half = value[halflength:]
                
                if first_half == second_half:
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
