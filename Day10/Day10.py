''' 
=============== Advent Day 10 ===============

The manual describes one machine per line. Each line contains a single indicator light diagram in [square brackets], one or more button wiring schematics in (parentheses), and joltage requirements in {curly braces}.
To start a machine, its indicator lights must match those shown in the diagram, where . means off and # means on. The machine has the number of indicator lights shown, but its indicator lights are all initially off.
So, an indicator light diagram like [.##.] means that the machine has four indicator lights which are initially off and that the goal is to simultaneously configure the first light to be off, the second light to be on, the third to be on, and the fourth to be off.
You can toggle the state of indicator lights by pushing any of the listed buttons. 
Each button lists which indicator lights it toggles, where 0 means the first light, 1 means the second light, and so on. When you push a button, each listed indicator light either turns on (if it was off) or turns off (if it was on). 
You have to push each button an integer number of times; there's no such thing as "0.5 presses" (nor can you push a button a negative number of times).
So, a button wiring schematic like (0,3,4) means that each time you push that button, the first, fourth, and fifth indicator lights would all toggle between on and off. If the indicator lights were [#.....], pushing the button would change them to be [...##.] instead.
Because none of the machines are running, the joltage requirements are irrelevant and can be safely ignored.
You can push each button as many times as you like. However, to save on time, you will need to determine the fewest total presses required to correctly configure all indicator lights for all machines in your list.
There are a few ways to correctly configure the first machine:

[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
You could press the first three buttons once each, a total of 3 button presses.
You could press (1,3) once, (2,3) once, and (0,1) twice, a total of 4 button presses.
You could press all of the buttons except (1,3) once each, a total of 5 button presses.
However, the fewest button presses required is 2. One way to do this is by pressing the last two buttons ((0,2) and (0,1)) once each.
Analyze each machine's indicator light diagram and button wiring schematics. What is the fewest button presses required to correctly configure the indicator lights on all of the machines?

============================================
'''

class Solution:
    def __init__(self):
        self.total_presses = 0

    def process_input(self, input):
        indicators = []
        schematic = []
        wiring = []
        wires = []
        indicator = []

        get_indicators = False
        get_wires = False

        for char in input:
            # Skip joltage for now
            # Skip commas and spaces
            if char == "{" or char == "}" or char == "," or char == " ":
                continue

            elif char == "\n":
                schematic.append(wiring)
                wiring = []
            
            # Handling [***] cases
            elif char == "[":
                get_indicators = True
            elif char == "]":
                get_indicators = False
                indicators.append(indicator)
                indicator = []

            # Handling (*), (*,*)... cases
            elif char == "(":
                get_wires = True
            elif char == ")":
                get_wires = False
                wiring.append(wires)
                wires = []

            elif get_indicators:
                if char == ".":
                    indicator.append(False)
                elif char == "#":
                    indicator.append(True)

            elif get_wires:
                wires.append(int(char))
        
        # Handle final case (no new line on last row)
        if wiring:
            schematic.append(wiring)

        return indicators, schematic
    
    # Convert the inputs to an array of booleans of same length as the indicators
    def convert_input_to_bool(self, inputs, indicator):
        converted = []

        for button in inputs:
            config = [False] * len(indicator)
            for idx in button:
                config[idx] = True
            converted.append(config)

        return converted

    # Solve the row (machine) by searching the possible configurations
    def solve_machine(self, indicator, inputs):
        button_presses = 0
        solved = False

        # initially all indicators are off
        start = [False]*len(indicator)

        if start == indicator:
            return 0

        possible_combinations = [start]
        visited = {tuple(start)}

        # This makes element wise addition of the two arrays easier
        bool_inputs = self.convert_input_to_bool(inputs, indicator)

        # We will search the graph of possible results by tracking the possible leaves at each level
        while not solved:
            button_presses += 1
            next_level = []

            for config in possible_combinations:
                for input in bool_inputs:
                    new_config = [c ^ m for c, m in zip(config, input)]
                    t = tuple(new_config)

                    # If already visited then don't save this state
                    if t in visited:
                        continue

                    # Check if we have solved the machine
                    if new_config == indicator:
                        return button_presses

                    visited.add(t)
                    next_level.append(new_config)

            possible_combinations = next_level

    def day_10(self, input):
        indicators, schematic = self.process_input(input)

        for i in range(len(schematic)):
            required_indicators = indicators[i]
            possible_inputs = schematic[i]
            # Solve each row (machine) of the puzzle one by one
            button_presses = self.solve_machine(required_indicators, possible_inputs)
            self.total_presses += button_presses

        return self.total_presses

if __name__ == "__main__":
    filename  = "Day10/input.txt"
    with open(filename, "r") as f:
        input = f.read()
    solver = Solution()
    result = solver.day_10(input)
    print(f"Day 10 solution: {result}")