from typing import TextIO

import click

from aoc2022.solutions.day6 import get_start_of_message_index


@click.command()
@click.argument("input_file", type=click.File())
def command(input_file: TextIO):
    line = input_file.readline()
    print(get_start_of_message_index(line.strip()))
