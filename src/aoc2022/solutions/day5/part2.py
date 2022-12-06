import re
from typing import TextIO

import click

from aoc2022.solutions.day5 import parse_crates, parse_moves


@click.command()
@click.argument("input_file", type=click.File())
def command(input_file: TextIO):
    stacks = parse_crates(input_file)
    line = input_file.readline()
    while line:
        crates_to_move, stack_from, stack_to = parse_moves(line)
        stacks[stack_to].extend(stacks[stack_from][len(stacks[stack_from]) - crates_to_move:len(stacks[stack_from])])
        stacks[stack_from] = stacks[stack_from][:len(stacks[stack_from]) - crates_to_move]
        line = input_file.readline()
    last_crates = "".join([stack[-1].letter if stack else " " for stack in stacks])
    print(last_crates)
