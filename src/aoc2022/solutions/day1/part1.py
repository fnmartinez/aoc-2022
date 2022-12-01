from typing import TextIO

import click

from aoc2022.solutions.day1 import Elf, elves_in_file


@click.command()
@click.argument("input_file", type=click.File())
def command(input_file: TextIO):
    most_caloric_elf: Elf = None
    for elf in elves_in_file(input_file):
        if not most_caloric_elf or (most_caloric_elf and most_caloric_elf.calories < elf.calories):
            most_caloric_elf = elf
    print(most_caloric_elf)
