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


class BootLoader:
    def __init__(self, data: list):
        self.data = data
        self.position = 0
        self.accumulator = 0
        self.commands = {
            "acc": self.__acc,
            "jmp": self.__jmp,
            "nop": self.__nop,
        }
        self.executed_positions = []

    def __acc(self, change_accumulator_by: int):
        """
        increases or decreases a single global value called the accumulator by the value given in
        the argument. For example, acc +7 would increase the accumulator by 7. The accumulator
        starts at 0. After an acc instruction, the instruction immediately below it is executed
        """
        self.accumulator += change_accumulator_by
        self.position = (self.position + 1) % len(self.data)

    def __jmp(self, jump: int):
        """
        jumps to a new instruction relative to itself. The next instruction to execute is found
        using the argument as an offset from the jmp instruction; for example, jmp +2 would skip
        the next instruction, jmp +1 would continue to the instruction immediately below it,
        and jmp -20 would cause the instruction 20 lines above to be executed next
        """
        self.position = (self.position + jump) % len(self.data)

    def __nop(self, nope: int):
        """
        stands for No Operation - it does nothing. The instruction immediately below it is
        executed next
        """
        self.position = (self.position + 1) % len(self.data)

    def execute(self):
        for _ in range(len(self.data)):
            comm_name = self.data[self.position][0]
            argument = self.data[self.position][-1]
            func = self.commands[comm_name]

            if self.position in self.executed_positions:
                break
            else:
                self.executed_positions.append(self.position)
            func(argument)


example_loader = BootLoader(parse_raw(EXAMPLE))
example_loader.execute()
print(example_loader.accumulator)

input_loader = BootLoader(parse_raw(INPUT))
input_loader.execute()
print(input_loader.accumulator)
