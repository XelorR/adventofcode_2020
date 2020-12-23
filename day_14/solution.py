import re
from itertools import product

EXAMPLE = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

with open("input.txt") as f:
    INPUT = f.read().strip()


# -= Part one =-

class Decoder:

    def __init__(self, data_raw: str):
        self.program = self.parse_raw(data_raw)
        self.mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        self.memory = {}

    def parse_raw(self, data_raw: str):
        data = [c.split(" = ") for c in data_raw.splitlines()]
        return [
            c if c[0] == "mask" else [int(re.findall(r"\d+", c[0])[0]), int(c[1])]
            for c in data
        ]

    def apply_mask(self, decimal: int) -> int:
        number = bin(decimal)[2:].zfill(36)
        return int("".join(
            [c if self.mask[i] == "X" else self.mask[i] for i, c in enumerate(number)]),
            2)

    def run_program(self):
        for c in self.program:
            if c[0] == "mask":
                self.mask = c[1]
            else:
                self.memory[c[0]] = self.apply_mask(c[1])

    def get_result(self):
        self.memory = {}
        self.run_program()
        return sum(self.memory.values())


example_decoder = Decoder(EXAMPLE)
assert example_decoder.get_result() == 165

part_one_decoder = Decoder(INPUT)
print("Part one answer is", part_one_decoder.get_result())


# -= Part two =-

class DecoderV2(Decoder):

    def apply_mask(self, decimal: int) -> list:
        number = bin(decimal)[2:].zfill(36)
        masked = []
        for i, c in enumerate(number):
            if self.mask[i] == "X":
                masked.append("X")
            elif self.mask[i] == "0":
                masked.append(str(c))
            else:
                masked.append("1")
        masked = "".join(masked)

        x_possible_variants = list(product("10", repeat=masked.count("X")))
        x_positions = [i for i, c in enumerate(masked) if c == "X"]
        possible_variants = []
        for i, v in enumerate(x_possible_variants):
            masked_list = [c for c in masked]
            for j, position in enumerate(x_positions):
                masked_list[position] = v[j]
            possible_variants.append(int("".join(masked_list), 2))
        return possible_variants

    def run_program(self):
        for c in self.program:
            if c[0] == "mask":
                self.mask = c[1]
            else:
                for mem in self.apply_mask(c[0]):
                    self.memory[mem] = c[1]


EXAMPLE_V2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

example_decoder_v2 = DecoderV2(EXAMPLE_V2)
assert example_decoder_v2.get_result() == 208

part_two_decoder = DecoderV2(INPUT)
print("Part two answer is", part_two_decoder.get_result())
