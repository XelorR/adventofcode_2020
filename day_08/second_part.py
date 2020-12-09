from copy import deepcopy

with open("input.txt", "r") as input_file:
    INPUT = input_file.read().strip()

EXAMPLE = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def parse_raw(data_raw: str) -> list:
    return [[row.split()[0], int(row.split()[1])] for row in data_raw.splitlines()]


example_data = parse_raw(EXAMPLE)
input_data = parse_raw(INPUT)


def switch_jmp_nop(instruction: str):
    if instruction == "nop":
        return "jmp"
    if instruction == "jmp":
        return "nop"


class BootLoader:
    def __init__(self, instructions: list):
        self.instructions = instructions
        self.position = 0
        self.accumulator = 0
        self.commands = {
            "acc": self.__acc,
            "jmp": self.__jmp,
            "nop": self.__nop,
        }
        self.executed_positions = []
        self.infinite_break = False
        self.possibly_changed_instructions = []

    def __acc(self, change_accumulator_by: int):
        """
        increases or decreases a single global value called the accumulator by the value given in
        the argument. For example, acc +7 would increase the accumulator by 7. The accumulator
        starts at 0. After an acc instruction, the instruction immediately below it is executed
        """
        self.accumulator += change_accumulator_by
        self.position = (self.position + 1) % len(self.instructions)

    def __jmp(self, jump: int):
        """
        jumps to a new instruction relative to itself. The next instruction to execute is found
        using the argument as an offset from the jmp instruction; for example, jmp +2 would skip
        the next instruction, jmp +1 would continue to the instruction immediately below it,
        and jmp -20 would cause the instruction 20 lines above to be executed next
        """
        self.position = (self.position + jump) % len(self.instructions)

    def __nop(self, nope: int):
        """
        stands for No Operation - it does nothing. The instruction immediately below it is
        executed next
        """
        self.position = (self.position + 1) % len(self.instructions)

    def execute(self, instructions=None):
        if instructions is None:
            instructions = deepcopy(self.instructions)
        self.position = 0
        self.accumulator = 0
        self.executed_positions = []
        self.infinite_break = False

        while True:
            comm_name = instructions[self.position][0]
            argument = instructions[self.position][-1]
            func = self.commands[comm_name]

            if self.position in self.executed_positions:
                self.infinite_break = True
                break
            else:
                if self.position + 1 == len(instructions):
                    self.infinite_break = False
                    self.executed_positions.append(self.position)
                    func(argument)
                    break
                self.executed_positions.append(self.position)
                func(argument)


def generate_possible_fixes(instructions: list) -> list:
    possible_versions = []
    i = 0
    for instruction, value in instructions:
        if instruction in ["nop", "jmp"]:
            temp_instr = deepcopy(instructions)
            temp_instr[i][0] = switch_jmp_nop(instruction)
            possible_versions.append(temp_instr)
        i += 1
    return possible_versions


def execute_correct_instruction(instructions):
    for instructions in generate_possible_fixes(instructions):
        loader = BootLoader(instructions)
        loader.execute()
        if not loader.infinite_break:
            return loader.accumulator


assert execute_correct_instruction(example_data) == 8
print("Value of the accumulator after the program terminates is",
      execute_correct_instruction(input_data))
