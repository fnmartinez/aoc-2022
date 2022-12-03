from typing import TextIO

import click

from aoc2022.solutions.day3 import LETTER_TO_PRIORITY


@click.command()
@click.argument("input_file", type=click.File())
def command(input_file: TextIO):
    backpack_content = input_file.readline()
    total_priority = 0
    while backpack_content:
        backpack_content = backpack_content.strip()
        pocket1, pocket2 = backpack_content[:len(backpack_content)//2], backpack_content[len(backpack_content)//2:]
        set_pocket1, set_pocket2 = set([l for l in pocket1]), set([l for l in pocket2])
        common_items = set_pocket1.intersection(set_pocket2)
        for item in common_items:
            total_priority += LETTER_TO_PRIORITY[item]
        backpack_content = input_file.readline()
    print(total_priority)
