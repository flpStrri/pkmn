from enum import Enum
from os.path import abspath


class Gen(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5


class Pokemon:
    number: int
    generation: Gen
    image_path: str

    @classmethod
    def do_we_gotta_catch_em_all(cls) -> bool:
        return True
