from typing import TextIO

import click

from aoc2022.solutions.day3 import LETTER_TO_PRIORITY


@click.command()
@click.argument("input_file", type=click.File())
def command(input_file: TextIO):
    line = input_file.readline()
    total_priority = 0
    while line:
        line = line.strip()
        backpack_group = [line, input_file.readline(), input_file.readline()]
        backpack_group_sets = [set([l for l in backpack]) for backpack in backpack_group]
        common_items = backpack_group_sets[0]
        for backpack_set in backpack_group_sets:
            common_items = common_items.intersection(backpack_set)
        for item in common_items:
            total_priority += LETTER_TO_PRIORITY[item]
        line = input_file.readline()
    print(total_priority)
