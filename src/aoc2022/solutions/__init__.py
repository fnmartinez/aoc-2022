from dataclasses import dataclass
from typing import TextIO


@dataclass
class Elf:
    no: int
    calories: int


def elves_in_file(input_file: TextIO):
    line = None
    more_elfs = True
    while more_elfs:
        new_elf = Elf(new_elf.no + 1, 0) if line else Elf(0, 0)
        line = input_file.readline()
        while line not in ("\n", ""):
            new_elf.calories += int(line.strip())
            line = input_file.readline()
        yield new_elf
        if line == "":
            more_elfs = False
