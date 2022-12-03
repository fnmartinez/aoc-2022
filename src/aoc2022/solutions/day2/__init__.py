from dataclasses import dataclass


@dataclass
class Hand:
    score: int
    loses_to = None
    wins_to = None

    def compare(self, other):
        if other == self:
            return None
        return other == self.wins_to

    def hand_for_result(self, result):
        lose_win_table = {
            None: self,
            True: self.wins_to,
            False: self.loses_to
        }
        return lose_win_table[result]


ROCK, PAPER, SCISSOR = Hand(1), Hand(2), Hand(3)

ROCK.loses_to, ROCK.wins_to = PAPER, SCISSOR
PAPER.loses_to, PAPER.wins_to = SCISSOR, ROCK
SCISSOR.loses_to, SCISSOR.wins_to = ROCK, PAPER

LETTER_TO_HAND = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSOR,
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSOR
}

LETTER_TO_RESULT = {
    "X": False,
    "Y": None,
    "Z": True
}

RESULT_SCORE = {
    False: 0,
    None: 3,
    True: 6
}
