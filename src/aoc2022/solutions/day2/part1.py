from typing import TextIO

import click

from aoc2022.solutions.day2 import LETTER_TO_HAND, RESULT_SCORE


@click.command()
@click.argument("input_file", type=click.File())
def command(input_file: TextIO):
    play = input_file.readline()
    total_score = 0
    while play:
        rhand_code, lhand_code = play.strip().split()
        rhand, lhand = LETTER_TO_HAND[rhand_code], LETTER_TO_HAND[lhand_code]
        result = lhand.compare(rhand)
        total_score += RESULT_SCORE[result] + lhand.score
        play = input_file.readline()
    print(total_score)
