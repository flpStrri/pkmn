from statistics import median
from typing import List

from domain.pokemon import Pokemon, Gen
from service.pkmn_image_manager import PkmnImageManager


def calculate_gen_one():
    print()
    pokemons = [Pokemon(i) for i in range(1, 151)]
    paths = [pokemon.image_path for pokemon in pokemons]
    pkmn_color_complexities: List[float] = [PkmnImageManager.get_complexity_from_path(path) for path in paths]
    gen_one_color_complexity = median(pkmn_color_complexities)
    _print_results(pokemons, pkmn_color_complexities, Gen.ONE, gen_one_color_complexity)


def _print_results(pokemons: List[Pokemon], complexities: List[float], generation: Gen, median_complexity: float):
    for pokemon in pokemons:
        print(f"Pokemon: {pokemon.name}, color complexity: {complexities[pokemon.number - 1]}")
    print(f"Generation: {generation}, median color complexity: {median_complexity}")


if __name__ == "__main__":
    calculate_gen_one()
