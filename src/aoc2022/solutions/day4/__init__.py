from dataclasses import dataclass


@dataclass
class Range:
    start: int
    end: int

    @classmethod
    def string_to_range(cls, s):
        return Range(*[int(n) for n in s.split("-")])


def ranges_fully_overlap(r1: Range, r2: Range):
    return ((r1.start <= r2.start and r2.end <= r1.end) or
            (r2.start <= r1.start and r1.end <= r2.end))


def ranges_overlap(r1: Range, r2: Range):
    return ((r1.start <= r2.start <= r1.end) or
            (r2.start <= r1.start <= r2.end))
