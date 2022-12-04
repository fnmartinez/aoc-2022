from typing import TextIO

import click

from aoc2022.solutions.day4 import Range, ranges_overlap


@click.command()
@click.argument("input_file", type=click.File())
def command(input_file: TextIO):
    line = input_file.readline()
    overlapping_couples = 0
    while line:
        line = line.strip()
        s1, s2 = line.split(",")
        r1, r2 = Range.string_to_range(s1), Range.string_to_range(s2)
        if ranges_overlap(r1, r2):
            overlapping_couples += 1
        line = input_file.readline()
    print(overlapping_couples)

