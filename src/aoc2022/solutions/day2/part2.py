from typing import TextIO

import click

from aoc2022.solutions.day2 import LETTER_TO_HAND, LETTER_TO_RESULT, RESULT_SCORE


@click.command()
@click.argument("input_file", type=click.File())
def command(input_file: TextIO):
    play = input_file.readline()
    total_score = 0
    while play:
        rcode, lcode = play.strip().split()
        rhand, result = LETTER_TO_HAND[rcode], LETTER_TO_RESULT[lcode]
        if result is None:
            lhand = rhand.hand_for_result(result)
        else:
            lhand = rhand.hand_for_result(not result)
        total_score += RESULT_SCORE[result] + lhand.score
        play = input_file.readline()
    print(total_score)
