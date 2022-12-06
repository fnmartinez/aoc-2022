import re

from dataclasses import dataclass
from typing import TextIO


@dataclass
class Crate:
    letter: str


def parse_crates(input_file: TextIO):
    crate_lines = list()
    line = input_file.readline()
    while line != "\n":
        crate_lines.append(line)
        line = input_file.readline()
    stacks = [[] for _ in range(len(re.split(r"\s+", crate_lines[-1].strip())))]
    for i in range(len(crate_lines) - 2, -1, -1):
        crates_rpr = re.findall(r"(\s{3}|\[\w\])\s", crate_lines[i])
        for stack_no, crate_rpr in enumerate(crates_rpr):
            crate_rpr = crate_rpr.strip()
            if crate_rpr:
                stacks[stack_no].append(Crate(re.findall(r"\[(\w)\]", crate_rpr)[0]))
    return stacks


def parse_moves(line):
    crates_to_move, stack_from, stack_to = (int(i) for i in re.findall(r"move (\d+) from (\d+) to (\d+)\n", line)[0])
    return crates_to_move, stack_from - 1, stack_to - 1
