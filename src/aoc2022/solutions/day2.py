from typing import TextIO

import click

from aoc2022.solutions import elves_in_file


TOP_N_ELVES = 3


@click.command()
@click.argument("input_file", type=click.File())
def command(input_file: TextIO):
    elves = [elf for elf in elves_in_file(input_file)]
    elves.sort(key=lambda elf: elf.calories, reverse=True)
    print(sum([elves[i].calories for i in range(TOP_N_ELVES)]))
