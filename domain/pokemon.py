from enum import Enum
from os.path import abspath
from pandas import read_csv


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

    def __init__(self, number: int):
        self.number = number
        self.generation = self.get_generation(number)
        self.image_path = self.get_image_path(number)
        self.name = self.get_name(number)

    @classmethod
    def do_we_gotta_catch_em_all(cls) -> bool:
        return True

    @classmethod
    def get_image_path(cls, number: int, back: bool = False, female: bool = False, shiny: bool = False) -> str:
        path = "data/images"
        path = path + "/back" if back else path
        path = path + "/shiny" if shiny else path
        path = path + "/female" if female else path
        path = path + "/" + str(number) + ".png"
        return abspath(path)

    @classmethod
    def get_generation(cls, number: int) -> Gen:
        pokedex = read_csv("data/pokemon.csv")
        generation = pokedex[pokedex["pokedex_number"] == number].iloc[0]["generation"]
        return Gen(generation)

    @classmethod
    def get_name(cls, number: int) -> str:
        pokedex = read_csv("data/pokemon.csv")
        name = pokedex[pokedex["pokedex_number"] == number].iloc[0]["japanese_name"]
        return name
