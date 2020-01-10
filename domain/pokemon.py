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

    @staticmethod
    def get_image_path(number: int, back: bool = False, female: bool = False, shiny: bool = False) -> str:
        path = ""
        path = path + "/back" if back else path
        path = path + "/shiny" if shiny else path
        path = path + "/female" if female else path
        path = path + "/" + str(number) + ".png"
        return abspath(path)
