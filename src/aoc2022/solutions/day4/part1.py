from typing import TextIO

import click

from aoc2022.solutions.day4 import Range, ranges_fully_overlap


@click.command()
@click.argument("input_file", type=click.File())
def command(input_file: TextIO):
    line = input_file.readline()
    fully_overlapping_couples = 0
    while line:
        line = line.strip()
        s1, s2 = line.split(",")
        r1, r2 = Range.string_to_range(s1), Range.string_to_range(s2)
        if ranges_fully_overlap(r1, r2):
            fully_overlapping_couples += 1
        line = input_file.readline()
    print(fully_overlapping_couples)
